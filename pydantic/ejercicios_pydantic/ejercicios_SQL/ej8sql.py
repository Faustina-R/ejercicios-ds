from datetime import datetime
from typing import List, Optional
from sqlalchemy import (
    create_engine,
    select,
    func,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Float,
    UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session


class Base(DeclarativeBase):
    pass


class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    cursos: Mapped[List["Curso"]] = relationship(back_populates="profesor")


class Curso(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    profesor_id: Mapped[Optional[int]] = mapped_column(ForeignKey("profesores.id"))

    profesor: Mapped[Optional["Profesor"]] = relationship(back_populates="cursos")
    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="curso")


class Estudiante(Base):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    legajo: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="estudiante")


class Inscripcion(Base):
    __tablename__ = "inscripciones"
    __table_args__ = (
        UniqueConstraint("estudiante_id", "curso_id", name="uq_estudiante_curso"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"))
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    calificacion_final: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    estudiante: Mapped["Estudiante"] = relationship(back_populates="inscripciones")
    curso: Mapped["Curso"] = relationship(back_populates="inscripciones")


engine = create_engine("sqlite:///universidad.db", echo=False)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Carga inicial de datos
with Session(engine) as session:
    p1 = Profesor(nombre="Alan Turing", email="alan@universidad.edu")
    p2 = Profesor(nombre="Ada Lovelace", email="ada@universidad.edu")

    c1 = Curso(titulo="Bases de Datos", profesor=p1)
    c2 = Curso(titulo="Algoritmos", profesor=p1)
    c3 = Curso(titulo="Programación en Python", profesor=p2)

    e1 = Estudiante(nombre="Carlos Ruiz", legajo="LEG-1001")
    e2 = Estudiante(nombre="María Gomez", legajo="LEG-1002")

    session.add_all([
        Inscripcion(estudiante=e1, curso=c1, calificacion_final=9.0),
        Inscripcion(estudiante=e1, curso=c2, calificacion_final=7.0),
        Inscripcion(estudiante=e2, curso=c1, calificacion_final=10.0),
    ])
    session.commit()

print("\n=== EJERCICIO 8: REPORTES ===")
with Session(engine) as session:
    #Cursos que dicta un profesor específico usando join
    print("1. Cursos de Alan Turing:")
    stmt1 = (
        select(Curso.titulo, Profesor.nombre)
        .join(Profesor, Curso.profesor_id == Profesor.id)
        .where(Profesor.nombre == "Alan Turing")
    )
    for titulo, profesor in session.execute(stmt1):
        print(f"   - {titulo} (Profesor: {profesor})")

    #Promedio de calificaciones de un estudiante específico (func.avg)
    stmt2 = (
        select(func.avg(Inscripcion.calificacion_final))
        .join(Estudiante, Inscripcion.estudiante_id == Estudiante.id)
        .where(Estudiante.nombre == "Carlos Ruiz")
    )
    promedio = session.scalar(stmt2)
    print(f"\n2. Promedio de Carlos Ruiz: {promedio:.2f}")

    #Contar estudiantes inscriptos por curso (func.count)
    print("\n3. Cantidad de inscriptos por curso:")
    stmt3 = (
        select(Curso.titulo, func.count(Inscripcion.id).label("inscriptos"))
        .outerjoin(Inscripcion, Curso.id == Inscripcion.curso_id)
        .group_by(Curso.id, Curso.titulo)
    )
    for titulo, total in session.execute(stmt3):
        print(f"   - {titulo}: {total} estudiante(s)")