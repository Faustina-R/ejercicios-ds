from datetime import datetime
from typing import List, Optional
from sqlalchemy import create_engine, select, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

class Base(DeclarativeBase):
    pass

class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    cursos: Mapped[List["Curso"]] = relationship(back_populates="profesor")

class Curso(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    creditos: Mapped[int] = mapped_column(Integer, default=3)

    profesor_id: Mapped[Optional[int]] = mapped_column(ForeignKey("profesores.id"))
    profesor: Mapped[Optional["Profesor"]] = relationship(back_populates="cursos")

    clases: Mapped[List["Clase"]] = relationship(
        back_populates="curso", cascade="all, delete-orphan"
    )

class Clase(Base):
    __tablename__ = "clases"

    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(150), nullable=False)
    duracion_minutos: Mapped[int] = mapped_column(Integer, nullable=False)

    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    curso: Mapped["Curso"] = relationship(back_populates="clases")


engine = create_engine("sqlite:///universidad.db", echo=False)
Base.metadata.drop_all(engine)  # Elimina tablas viejas desactualizadas
Base.metadata.create_all(engine)  # Crea las tablas con el esquema nuevo

print("\n=== EJERCICIO 5: CLASES DE UN CURSO ===")
with Session(engine) as session:
    # 1. Crear profesor y curso vinculado
    prof = Profesor(nombre="Alan Turing", email="alan@universidad.edu")
    curso_bd = Curso(titulo="Bases de Datos", creditos=6, profesor=prof)
    
    # 2. Crear clases vinculadas al curso
    clase1 = Clase(tema="Modelado Entidad-Relación", duracion_minutos=120, curso=curso_bd)
    clase2 = Clase(tema="Normalización y Formas Normales", duracion_minutos=90, curso=curso_bd)
    clase3 = Clase(tema="SQL DDL y DML", duracion_minutos=120, curso=curso_bd)

    session.add_all([prof, curso_bd, clase1, clase2, clase3])
    session.commit()

    # 3. Consulta a través del ORM
    curso_consultado = session.scalars(
        select(Curso).where(Curso.titulo == "Bases de Datos")
    ).first()

    if curso_consultado:
        print(f"Curso: {curso_consultado.titulo}")
        for c in curso_consultado.clases:
            print(f"  * Clase: {c.tema} | Duración: {c.duracion_minutos} min")
