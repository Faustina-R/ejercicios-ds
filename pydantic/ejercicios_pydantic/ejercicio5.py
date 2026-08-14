from typing import Optional, List, Union
from pydantic import BaseModel, Field, HttpUrl, ValidationError

class PerfilUsuario(BaseModel):
    username: str = Field(
        pattern=r"^[a-z0-9_]{3,20}$",
        description="Entre 3 y 20 caracteres en minúscula, números o guion bajo"
    )
    biografia: Optional[str] = Field(default=None, max_length=200)
    redes_sociales: Optional[List[Union[HttpUrl, str]]] = Field(default_factory=list)

print("=== EJERCICIO 5: CASOS DE PRUEBA ===")

# Caso Válido
try:
    perfil = PerfilUsuario(
        username="dev_martin",
        biografia="Desarrollador backend aprendiendo validación de datos.",
        redes_sociales=["https://github.com/dev_martin", "https://linkedin.com"]
    )
    print(" Perfil creado con éxito:")
    print(perfil.model_dump())
except ValidationError as e:
    print(e)

# Caso Inválido
print("\n Error esperado: Validación de username (pattern) y longitud máxima")
try:
    PerfilUsuario(
        username="UsuarioConMayusculas!",
        biografia="a" * 210
    )
except ValidationError as e:
    print(e)