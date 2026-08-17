#!/usr/bin/env python3
"""Ejercicio 4: Convierte temperaturas entre Celsius y Fahrenheit."""


def celsius_a_fahrenheit(valor):
    return (valor * 9 / 5) + 32


def fahrenheit_a_celsius(valor):
    return (valor - 32) * 5 / 9


def main():
    valor = float(input("Ingrese el valor de temperatura: "))
    escala = input("Ingrese la escala original (C/F): ").strip().upper()

    if escala == "C":
        convertido = celsius_a_fahrenheit(valor)
        print(f"{valor}°C equivalen a {convertido:.2f}°F")
    elif escala == "F":
        convertido = fahrenheit_a_celsius(valor)
        print(f"{valor}°F equivalen a {convertido:.2f}°C")
    else:
        print("Escala no reconocida. Ingrese 'C' o 'F'.")


if __name__ == "__main__":
    main()
