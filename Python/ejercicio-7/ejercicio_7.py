#!/usr/bin/env python3
"""Ejercicio 7: Menú interactivo usando la estructura match."""


def suma_primeros_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def divisibles_por_3(inicio, fin):
    return [n for n in range(inicio, fin + 1) if n % 3 == 0]


def main():
    while True:
        print("\n--- Menú ---")
        print("1. Sumar los primeros N números naturales")
        print("2. Encontrar números divisibles por 3 en un rango")
        print("3. Salir")

        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                n = int(input("Ingrese N: "))
                print(f"La suma de los primeros {n} números naturales es: {suma_primeros_n(n)}")
            case "2":
                inicio = int(input("Ingrese el inicio del rango: "))
                fin = int(input("Ingrese el fin del rango: "))
                resultado = divisibles_por_3(inicio, fin)
                print(f"Números divisibles por 3 entre {inicio} y {fin}: {resultado}")
            case "3":
                print("Hasta luego")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
