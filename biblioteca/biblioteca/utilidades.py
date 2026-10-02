import math
import random


def generar_codigo_prestamo(usados=()):
    # PR-xxxx, se repite si ya salió ese número
    while True:
        codigo = f"PR-{random.randint(1000, 9999)}"
        if codigo not in usados:
            return codigo


def dias_a_semanas(dias):
    if dias < 0:
        raise ValueError("Los días de retraso no pueden ser negativos.")
    return math.ceil(dias / 7)  # redondeo hacia arriba


def codificar_titulo(titulo):
    titulo = titulo.strip()
    letras = "".join(caracter for caracter in titulo if caracter.isalpha())
    if not letras:
        raise ValueError("El título debe contener al menos una letra.")
    # 3 letras + suma de ord() % 1000
    prefijo = letras[:3].upper().ljust(3, "X")
    suma = sum(ord(caracter) for caracter in titulo) % 1000
    return f"{prefijo}-{suma:03d}"


if __name__ == "__main__":
    print("Prueba rápida de utilidades.py")
    print(generar_codigo_prestamo())
    print(codificar_titulo("Python Essentials"))
    print(codificar_titulo("C"))
    for dias in (0, 1, 7, 8, 15):
        print(f"{dias} días de retraso -> {dias_a_semanas(dias)} semana(s)")
