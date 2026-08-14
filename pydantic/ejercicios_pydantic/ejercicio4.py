from pydantic import BaseModel, Field, EmailStr, ValidationError

class UsuarioSistema(BaseModel):
    email: EmailStr
    nivel_acceso: int = Field(ge=1, le=5)

print("=== EJERCICIO 4: CAPTURA DE EXCEPCIONES ===")

datos_invalidos = {
    "email": "correo_invalido_sin_dominio",
    "nivel_acceso": 9
}

try:
    usuario = UsuarioSistema(**datos_invalidos)
except ValidationError as error:
    print(" ValidationError capturado correctamente.")
    print("\nDetalle de errores detectados:")
    for err in error.errors():
        campo = err["loc"][0]
        mensaje = err["msg"]
        tipo = err["type"]
        print(f" • Campo afectado: '{campo}' | Mensaje: {mensaje} | Tipo de fallo: {tipo}")