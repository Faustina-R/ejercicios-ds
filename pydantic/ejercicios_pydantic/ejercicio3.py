from typing import Annotated, Optional
from pydantic import BaseModel, Field, ValidationError

# Defino el tipo reutilizable con Annotated
CoordenadaGPS = Annotated[float, Field(ge=-90.0, le=90.0, description="Rango válido: [-90.0, 90.0]")]

class Ubicacion(BaseModel):
    latitud: CoordenadaGPS
    longitud: CoordenadaGPS
    etiqueta: Optional[str] = None

print("=== EJERCICIO 3: CASOS DE PRUEBA ===")

# Caso Válido
try:
    pto = Ubicacion(latitud=-43.3002, longitud=-65.1023, etiqueta="Oficina Central")
    print(" Ubicación válida creada:")
    print(pto.model_dump())
except ValidationError as e:
    print(e)

# Caso Inválido: Latitud fuera de rango (> 90.0)
print("\n Error esperado: Coordenada fuera de rango (-90 a 90)")
try:
    Ubicacion(latitud=135.0, longitud=45.0)
except ValidationError as e:
    print(e)