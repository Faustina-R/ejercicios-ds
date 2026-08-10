#!/usr/bin/env python3
"""Ejercicio 5: Verifica si una contraseña cumple con condiciones básicas
de seguridad (longitud mínima, mayúscula y minúscula)."""


def main():
    contrasena = input("Ingrese una contraseña: ")

    tiene_longitud = len(contrasena) >= 8
    tiene_mayuscula = any(c.isupper() for c in contrasena)
    tiene_minuscula = any(c.islower() for c in contrasena)

    if tiene_longitud and tiene_mayuscula and tiene_minuscula:
        print("La contraseña es válida.")
    else:
        print("La contraseña no es válida. Debe cumplir:")
        if not tiene_longitud:
            print("- Tener al menos 8 caracteres.")
        if not tiene_mayuscula:
            print("- Contener al menos una letra mayúscula.")
        if not tiene_minuscula:
            print("- Contener al menos una letra minúscula.")


if __name__ == "__main__":
    main()
