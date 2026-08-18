from typing import List
from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

class Base(DeclarativeBase):
    pass

class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()

    cursos: Mapped[List["Curso"]] = relationship(back_populates="profesor")

class Curso(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column()
    creditos: Mapped[int] = mapped_column()
    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))

    profesor: Mapped["Profesor"] = relationship(back_populates="cursos")

engine = create_engine("sqlite:///universidad.db")
Base.metadata.create_all(engine)

#Inserción de prueba
with Session(engine) as session:
    profe = Profesor(nombre="Alan Turing", email="alan@mail.com")
    c1 = Curso(titulo="Estructuras de Datos", creditos=6, profesor=profe)
    c2 = Curso(titulo="Algoritmos Complejos", creditos=8, profesor=profe)

    session.add(profe)
    session.commit()

#Consulto los cursos del profesor
with Session(engine) as session:
    profesores = session.scalars(select(Profesor)).all()
    for p in profesores:
        print(f"Profesor: {p.nombre}")
        for c in p.cursos:
            print(f" - Dicta: {c.titulo} ({c.creditos} créditos)")