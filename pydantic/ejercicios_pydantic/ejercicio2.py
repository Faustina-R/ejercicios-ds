from typing import Union, Literal
from pydantic import BaseModel, ValidationError

class Dispositivo(BaseModel):
    id_dispositivo: Union[int, str]
    tipo: Literal["sensor", "actuador", "gateway"]

print("=== EJERCICIO 2: CASOS DE PRUEBA ===")

# Caso Válido 1: id como entero
d1 = Dispositivo(id_dispositivo = 450, tipo = "sensor")
print(f" Válido (id numérico): {d1}")

# Caso Válido 2: id como texto (UUID / Serial)
d2 = Dispositivo(id_dispositivo = " SN-9982-X ", tipo = "gateway")
print(f" Válido (id string): {d2}")

# Caso Inválido: tipo no permitido en el Literal
print("\n Error esperado: Tipo de dispositivo no permitido")
try:
    Dispositivo(id_dispositivo = 101, tipo = " camara ") # type: ignore
except ValidationError as e:
    print(e)