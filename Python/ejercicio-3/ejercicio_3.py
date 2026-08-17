#!/usr/bin/env python3
"""Ejercicio 3: Calcula el costo total de un viaje y verifica si el dinero
disponible alcanza para cubrirlo."""


def main():
    costo_pasaje = float(input("Costo estimado del pasaje: $"))
    costo_alojamiento_noche = float(input("Costo del alojamiento por noche: $"))
    cantidad_noches = int(input("Cantidad de noches: "))
    dinero_disponible = float(input("Dinero disponible: $"))

    costo_total = costo_pasaje + (costo_alojamiento_noche * cantidad_noches)
    alcanza = dinero_disponible >= costo_total

    print("\n--- Resumen del viaje ---")
    print(f"Costo del pasaje: ${costo_pasaje:.2f}")
    print(f"Costo de alojamiento ({cantidad_noches} noches): "
          f"${costo_alojamiento_noche * cantidad_noches:.2f}")
    print(f"Costo total del viaje: ${costo_total:.2f}")
    print(f"Dinero disponible: ${dinero_disponible:.2f}")
    print(f"¿Alcanza el dinero disponible? {'Sí' if alcanza else 'No'}")

    if not alcanza:
        faltante = costo_total - dinero_disponible
        print(f"Te faltarían ${faltante:.2f}")


if __name__ == "__main__":
    main()
