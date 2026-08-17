#!/usr/bin/env python3
"""Ejercicio 6: Simula un inicio de sesión con un máximo de 3 intentos."""

CONTRASENA_CORRECTA = "Admin1234"
MAX_INTENTOS = 3


def main():
    intentos = 0

    while intentos < MAX_INTENTOS:
        contrasena = input("Ingrese la contraseña: ")

        if contrasena == CONTRASENA_CORRECTA:
            print("Inicio de sesión exitoso. ¡Bienvenido/a!")
            return

        intentos += 1
        intentos_restantes = MAX_INTENTOS - intentos

        if intentos_restantes > 0:
            print(f"Contraseña incorrecta. Intentos restantes: {intentos_restantes}")

    print("Se agotaron los intentos. Cuenta bloqueada.")


if __name__ == "__main__":
    main()
