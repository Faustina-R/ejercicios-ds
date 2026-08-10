#!/usr/bin/env python3
"""Ejercicio 8: Analiza una lista de temperaturas y retorna máximo, mínimo
y promedio en una tupla."""


def analizar_temperaturas(registros):
    maximo = max(registros)
    minimo = min(registros)
    promedio = sum(registros) / len(registros)
    return (maximo, minimo, promedio)


def main():
    temperaturas_prueba = [18.5, 22.0, 19.8, 25.3, 15.6, 20.1]

    maximo, minimo, promedio = analizar_temperaturas(temperaturas_prueba)

    print(f"Temperaturas: {temperaturas_prueba}")
    print(f"Máxima: {maximo}°C")
    print(f"Mínima: {minimo}°C")
    print(f"Promedio: {promedio:.2f}°C")


if __name__ == "__main__":
    main()
