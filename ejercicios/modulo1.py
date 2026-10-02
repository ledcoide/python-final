# Parte 1: módulos, paquetes y PIP
# python modulo1.py  (desde la carpeta ejercicios/)

import math
import platform
import random

from herramientas import conversiones, textos


def titulo(texto):
    print(f"\n=== {texto} ===")


# 1. Calculadora geométrica
def calculadora_geometrica():
    titulo("1. Calculadora geométrica")
    while True:
        entrada = input("Radio del círculo: ").strip()
        try:
            radio = float(entrada)
        except ValueError:
            print(f"'{entrada}' no es un número. Intenta de nuevo.")
            continue
        if radio < 0 or not math.isfinite(radio):
            print("El radio debe ser un número finito y no negativo.")
            continue
        break

    area = math.pi * radio ** 2
    circunferencia = 2 * math.pi * radio
    print(f"Área: {round(area, 2)}")
    print(f"Circunferencia: {round(circunferencia, 2)}")
    print(f"math.floor(área) = {math.floor(area)}   math.ceil(área) = {math.ceil(area)}")


# 2. Lotería
def loteria():
    titulo("2. Lotería")
    random.seed(2026)  # misma jugada cada vez que se corre
    numeros = sorted(random.sample(range(1, 41), 6))
    print("Números ganadores:", numeros)


# 3. Diagnóstico del equipo
def diagnostico():
    titulo("3. Diagnóstico del equipo")
    print("Sistema operativo:", platform.system())
    print("Versión del SO:   ", platform.release(), "|", platform.version())
    print("Arquitectura:     ", platform.machine(), platform.architecture()[0])
    print("Procesador:       ", platform.processor() or "(no disponible)")
    print("Python:           ", platform.python_version(), f"({platform.python_implementation()})")


# 4. Exploración de math
def exploracion():
    titulo("4. Funciones de math que empiezan con 'is'")
    funciones = [nombre for nombre in dir(math)
                 if nombre.startswith("is") and callable(getattr(math, nombre))]
    print(funciones)


# 5. Paquete propio
def paquete_propio():
    titulo("5. Paquete propio 'herramientas'")
    print(f"25 °C = {conversiones.celsius_a_fahrenheit(25):.1f} °F")
    print(f"77 °F = {conversiones.fahrenheit_a_celsius(77):.1f} °C")
    print(f"10 km = {conversiones.km_a_millas(10):.2f} millas")
    print(f"26.2 millas = {conversiones.millas_a_km(26.2):.2f} km")
    frase = "Instituto Tecnológico de Las Américas"
    print(f"Vocales en '{frase}': {textos.contar_vocales(frase)}")
    print(f"Invertido: {textos.invertir_texto(frase)}")


# 6. PIP: colorama (pip install colorama)
def mensaje_en_color():
    titulo("6. PIP — mensaje en color con colorama")
    try:
        from colorama import Fore, Style, init
    except ImportError:
        print("colorama no está instalado. Ejecuta: python -m pip install colorama")
        return
    init()  # colores en Windows
    print(Fore.GREEN + "¡Práctica final de Python Essentials 2!" + Style.RESET_ALL)
    print(Fore.CYAN + "ITLA" + Fore.YELLOW + " · Santo Domingo" + Style.RESET_ALL)


# Pregunta de análisis: __name__ al ejecutar vs. al importar
def demostrar_name():
    titulo("Análisis: __name__")
    print(f"En este archivo, __name__ = {__name__!r}")
    print(f"En el módulo importado, conversiones.__name__ = {conversiones.__name__!r}")
    print("Si se ejecuta 'python -c \"import modulo1\"', aquí se imprimiría 'modulo1'")
    print("y main() no correría, porque el bloque if __name__ == '__main__' sería falso.")


def main():
    calculadora_geometrica()
    loteria()
    diagnostico()
    exploracion()
    paquete_propio()
    mensaje_en_color()
    demostrar_name()


print(f"[modulo1] cargado con __name__ = {__name__!r}")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nEjecución interrumpida por el usuario.")
