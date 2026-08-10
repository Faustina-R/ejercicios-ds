#!/usr/bin/env python3
"""Ejercicio 9: Calcula el precio final de un producto aplicando descuento
general y un descuento extra para clientes VIP."""


def calcular_precio_final(precio_base, porcentaje_descuento=10, es_vip=False):
    if precio_base <= 0 or porcentaje_descuento < 0:
        raise ValueError("El precio base y el descuento deben ser valores positivos.")

    precio_con_descuento = precio_base * (1 - porcentaje_descuento / 100)

    if es_vip:
        precio_con_descuento *= (1 - 5 / 100)

    return round(precio_con_descuento, 2)


def main():
    casos = [
        {"precio_base": 1000, "porcentaje_descuento": 10, "es_vip": False},
        {"precio_base": 1000, "porcentaje_descuento": 10, "es_vip": True},
        {"precio_base": 500, "porcentaje_descuento": 20, "es_vip": True},
        {"precio_base": 2500, "es_vip": False},  # usa descuento por defecto (10%)
    ]

    for caso in casos:
        precio_final = calcular_precio_final(**caso)
        print(f"{caso} -> Precio final: ${precio_final}")

    try:
        calcular_precio_final(-100)
    except ValueError as e:
        print(f"Error esperado al ingresar un valor inválido: {e}")


if __name__ == "__main__":
    main()
