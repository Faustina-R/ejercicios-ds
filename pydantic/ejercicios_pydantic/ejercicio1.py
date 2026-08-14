from pydantic import BaseModel, Field, EmailStr, ValidationError

class Estudiante(BaseModel):
    legajo: int = Field(gt=0, description="Debe ser mayor a 0")
    nombre_completo: str = Field(min_length=5, description="Mínimo 5 caracteres")
    email: EmailStr
    promedio: float = Field(default=0.0, ge=0.0, le=10.0)

print("=== EJERCICIO 1: CASOS DE PRUEBA ===")

# Caso Válido
try:
    estudiante_ok = Estudiante(
        legajo=1024,
        nombre_completo="Carlos Benitez",
        email="carlos@example.com",
        promedio=7.5
    )
    print("\n Instancia válida creada:")
    print(estudiante_ok)
except ValidationError as e:
    print(e)

# Errores para observar los mensajes de validación
casos_error = [
    ("Legajo no positivo", {"legajo": -1, "nombre_completo": "Carlos Benitez", "email": "carlos@example.com"}),
    ("Nombre muy corto", {"legajo": 100, "nombre_completo": "Ana", "email": "ana@example.com"}),
    ("Email con formato inválido", {"legajo": 100, "nombre_completo": "Ana Gomez", "email": "esto-no-es-un-email"}),
    ("Promedio mayor a 10", {"legajo": 100, "nombre_completo": "Ana Gomez", "email": "ana@example.com", "promedio": 12.0})
]

for motivo, data in casos_error:
    print(f"\n Error esperado: {motivo}")
    try:
        Estudiante(**data)
    except ValidationError as e:
        print(e)