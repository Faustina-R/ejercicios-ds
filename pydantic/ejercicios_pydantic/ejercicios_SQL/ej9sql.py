from datetime import datetime
from typing import Optional
from sqlalchemy import (
    create_engine,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Float,
    UniqueConstraint,
)
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session


class Base(DeclarativeBase):
    pass


class Estudiante(Base):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    legajo: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)


class Curso(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)


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


engine = create_engine("sqlite:///universidad.db", echo=False)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Carga de datos base
with Session(engine) as session:
    e1 = Estudiante(nombre="Carlos Ruiz", legajo="LEG-1001")
    c1 = Curso(titulo="Bases de Datos")
    session.add_all([e1, c1])
    session.commit()


def matricular_alumno(estudiante_id: int, curso_id: int):
    with Session(engine) as session:
        try:
            nueva_inscripcion = Inscripcion(
                estudiante_id=estudiante_id,
                curso_id=curso_id
            )
            session.add(nueva_inscripcion)
            session.commit()
            print(f"[OK] Estudiante {estudiante_id} matriculado con éxito en Curso {curso_id}.")
        except IntegrityError as e:
            session.rollback()
            print(f"[ERROR / ROLLBACK] Integridad violada (alumno ya matriculado): {e.orig}")
        except SQLAlchemyError as e:
            session.rollback()
            print(f"[ERROR / ROLLBACK] Fallo de BD: {e}")


print("\n=== EJERCICIO 9: PRUEBA TRANSACCIONAL ===")
#Primera matriculación (éxito)
matricular_alumno(estudiante_id=1, curso_id=1)

#Segunda matriculación idéntica (fuerza la excepción y dispara el rollback)
matricular_alumno(estudiante_id=1, curso_id=1)