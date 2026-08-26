from datetime import datetime
from typing import List 
from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

#Clase base de la que heredan todos los modelos 
class Base(DeclarativeBase):
    pass

#defino el modelo de departamento
class Departamento(Base):
    __tablename__ = "Departamentos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column()
    
    #uso relationship() para acceder a la lista de profesores
    profesores: Mapped[List["Profesor"]] = relationship()

#defino el modelo de profesor
class Profesor(Base):
    __tablename__ = "Profesores"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    fecha_ingreso: Mapped[datetime] = mapped_column(default=datetime.now)
    
    #clave foranea fisica hacia la tabla departamentos
    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))


#conxion a la base de datos SQLite
engine = create_engine("sqlite:///universidad.db")
Base.metadata.create_all(engine)

#inserto un departamento con profesores
with Session(engine) as session: 
    depto = Departamento(nombre="Informática")
    session.add(depto)
    session.commit()
    
    p1 = Profesor(nombre="Ana Torres", email="ana@mail.com", departamento_id=depto.id)
    p2 = Profesor(nombre="Marcos Ruiz", email="marcos@mail.com", departamento_id=depto.id)
    session.add_all([p1, p2])
    session.commit()
    
#muestro los profesores desde el departamento
with Session(engine) as session:
    deptos = session.scalars(select(Departamento)).all()
    for d in deptos:
        print(f"Departamento: {d.nombre}")
        for prof in d.profesores:
            print(f" - Profesor: {prof.nombre} ({prof.email})")
            
            