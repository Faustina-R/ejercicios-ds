from datetime import datetime
from typing import List
from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

# 1. Base declarativa
class Base(DeclarativeBase):
    pass

# 2. Modelo Departamento (debe tener __tablename__ = "departamentos")
class Departamento(Base):
    __tablename__ = "departamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column()

    # Relación para acceder a la lista de profesores
    profesores: Mapped[List["Profesor"]] = relationship()

# 3. Modelo Profesor (apunta a departamentos.id)
class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    fecha_ingreso: Mapped[datetime] = mapped_column(default=datetime.now)
    
    # Clave foránea que apunta a la tabla departamentos
    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))

# 4. Creación del motor y las tablas
engine = create_engine("sqlite:///universidad.db")
Base.metadata.create_all(engine)

# 5. Insertar departamento con profesores
with Session(engine) as session:
    depto = Departamento(nombre="Informática")
    session.add(depto)
    session.commit()

    p1 = Profesor(nombre="Ana Torres", email="ana@mail.com", departamento_id=depto.id)
    p2 = Profesor(nombre="Marcos Ruiz", email="marcos@mail.com", departamento_id=depto.id)
    session.add_all([p1, p2])
    session.commit()

# 6. Mostrar por consola
with Session(engine) as session:
    deptos = session.scalars(select(Departamento)).all()
    print("=== EJERCICIO 2: Departamentos y Profesores ===")
    for d in deptos:
        print(f"Departamento: {d.nombre}")
        for prof in d.profesores:
            print(f"  - {prof.nombre} ({prof.email})")