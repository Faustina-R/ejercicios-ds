from pydantic import BaseModel, Field, EmailStr, ValidationError

class Estudiante(BaseModel):
    legajo: int = Field(gt=0, description="Debe ser un entero positivo")
    nombre_completo: str = Field(min_length=5)
    email: EmailStr
    promedio: float = Field(default=0.0, ge=0.0, le=10.0)

# 1. Instancia válida
try:
    alumno_ok = Estudiante(
        legajo=1054,
        nombre_completo="Juan Perez",
        email="juan.perez@example.com",
        promedio=8.5
    )
    print("Estudiante válido:", alumno_ok)
except ValidationError as e:
    print(e)

# 2. Error en legajo (negativo o cero)
print("\n--- Test Error Legajo ---")
try:
    Estudiante(legajo=-5, nombre_completo="Juan Perez", email="juan@mail.com")
except ValidationError as e:
    print(e)

# 3. Error en nombre_completo (menos de 5 caracteres)
print("\n--- Test Error Nombre Completo ---")
try:
    Estudiante(legajo=1, nombre_completo="Ana", email="ana@mail.com")
except ValidationError as e:
    print(e)

# 4. Error en email (formato inválido)
print("\n--- Test Error Email ---")
try:
    Estudiante(legajo=1, nombre_completo="Ana Garcia", email="correo-invalido")
except ValidationError as e:
    print(e)

# 5. Error en promedio (fuera de rango > 10.0)
print("\n--- Test Error Promedio ---")
try:
    Estudiante(legajo=1, nombre_completo="Ana Garcia", email="ana@mail.com", promedio=11.5)
except ValidationError as e:
    print(e)