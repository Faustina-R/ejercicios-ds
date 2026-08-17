#!/usr/bin/env python3
"""Ejercicio 2: Saluda usando el primer argumento recibido por la terminal"""

import sys


def main():
    if len(sys.argv) < 2:
        print("Uso: python ejercicio_2.py <nombre>")
        return

    nombre = sys.argv[1]
    print(f"¡Hola {nombre.capitalize()}!")


if __name__ == "__main__":
    main()
