from datetime import datetime
from typing import List, Optional
from sqlalchemy import (
    create_engine,
    select,
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


class Estudiante(Base):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    legajo: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    inscripciones: Mapped[List["Inscripcion"]] = relationship(
        back_populates="estudiante", cascade="all, delete-orphan"
    )


class Curso(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    creditos: Mapped[int] = mapped_column(Integer, default=3)

    inscripciones: Mapped[List["Inscripcion"]] = relationship(
        back_populates="curso", cascade="all, delete-orphan"
    )


class Inscripcion(Base):
    __tablename__ = "inscripciones"
    __table_args__ = (
        UniqueConstraint("estudiante_id", "curso_id", name="uq_estudiante_curso"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"))
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    fecha_inscripcion: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    calificacion_final: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    estudiante: Mapped["Estudiante"] = relationship(back_populates="inscripciones")
    curso: Mapped["Curso"] = relationship(back_populates="inscripciones")


engine = create_engine("sqlite:///universidad.db", echo=False)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

print("\n=== EJERCICIOS 6 Y 7: INSCRIPCIONES ===")
with Session(engine) as session:
    c1 = Curso(titulo="Bases de Datos", creditos=6)
    c2 = Curso(titulo="Programación en Python", creditos=4)

    e1 = Estudiante(nombre="Carlos Ruiz", legajo="LEG-1001")
    e2 = Estudiante(nombre="María Gomez", legajo="LEG-1002")

    # Inscripción enriquecida con fecha y nota
    i1 = Inscripcion(estudiante=e1, curso=c1, calificacion_final=9.5)
    i2 = Inscripcion(estudiante=e1, curso=c2, calificacion_final=8.0)
    i3 = Inscripcion(estudiante=e2, curso=c1, calificacion_final=7.5)

    session.add_all([c1, c2, e1, e2, i1, i2, i3])
    session.commit()

    # Verificación
    for est in session.scalars(select(Estudiante)).all():
        print(f"\nEstudiante: {est.nombre} (Legajo: {est.legajo})")
        for ins in est.inscripciones:
            print(f"  - Curso: {ins.curso.titulo} | Nota: {ins.calificacion_final} | Fecha: {ins.fecha_inscripcion.strftime('%Y-%m-%d')}")