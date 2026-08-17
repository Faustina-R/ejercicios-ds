from datetime import datetime
from typing import List
from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

#Base declarativa
class Base(DeclarativeBase):
    pass

#Modelo Departamento
class Departamento(Base):
    __tablename__ = "departamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column()

    # Relación bidireccional hacia profesores
    profesores: Mapped[List["Profesor"]] = relationship(back_populates="departamento")

#Modelo Profesor
class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    fecha_ingreso: Mapped[datetime] = mapped_column(default=datetime.now)
    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))

    # Relación bidireccional hacia departamento
    departamento: Mapped["Departamento"] = relationship(back_populates="profesores")

#Creación de motor y tablas
engine = create_engine("sqlite:///universidad.db")
Base.metadata.create_all(engine)

#Inserción: 1 departamento con 3 profesores
with Session(engine) as session:
    depto_exactas = Departamento(nombre="Ciencias Exactas")
    
    p1 = Profesor(nombre="Esteban Quito", email="esteban@mail.com", departamento=depto_exactas)
    p2 = Profesor(nombre="Elena Nito", email="elena@mail.com", departamento=depto_exactas)
    p3 = Profesor(nombre="Faus Pro", email="fausss@mail.com", departamento=depto_exactas)

    session.add(depto_exactas)
    session.commit()

#Consultas y navegación bidireccional
with Session(engine) as session:
   
    print("=== EJERCICIO 3: Navegación ===")

    #Desde Departamento -> Profesores
    stmt_depto = select(Departamento).where(Departamento.nombre == "Ciencias Exactas")
    depto = session.scalars(stmt_depto).first()
    
    if depto is not None:
        print(f"Profesores del depto '{depto.nombre}':")
        for prof in depto.profesores:
            print(f" -> {prof.nombre}")

    #Desde Profesor -> Departamento
    stmt_profe = select(Profesor).where(Profesor.nombre == "Esteban Quito")
    profe = session.scalars(stmt_profe).first()

    if profe is not None:
        print(f"\nEl profesor {profe.nombre} pertenece a: {profe.departamento.nombre}")
