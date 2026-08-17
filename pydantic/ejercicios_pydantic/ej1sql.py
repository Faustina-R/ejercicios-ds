from datetime import datetime
from sqlalchemy import create_engine, DateTime, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# 1. Base declarativa
class Base(DeclarativeBase):
    pass

# 2. Modelo Profesor
class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"Profesor(id={self.id}, nombre='{self.nombre}', email='{self.email}', ingreso={self.fecha_ingreso.date()})"

# 3. Engine 
engine = create_engine("sqlite:///:memory:", echo=False)
Base.metadata.create_all(engine)

# 4. Inserción y consulta
with Session(engine) as session:
    p1 = Profesor(nombre="Carlos Gomez", email="carlos.gomez@uni.edu", fecha_ingreso=datetime(2021, 3, 15))
    p2 = Profesor(nombre="Laura Fernandez", email="laura.f@uni.edu", fecha_ingreso=datetime(2023, 8, 1))
    
    session.add_all([p1, p2])
    session.commit()

    # Consulta SELECT 
    profesores = session.scalars(select(Profesor)).all()
    print("=== EJERCICIO 1: Profesores Registrados ===")
    for prof in profesores:
        print(prof)