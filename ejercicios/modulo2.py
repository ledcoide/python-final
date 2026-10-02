# Parte 2: strings, listas y excepciones
# python modulo2.py  (desde ejercicios/)

import math


def titulo(texto):
    print(f"\n=== {texto} ===")


# 1. Cifrado César
def cesar(texto, desplazamiento):
    # solo mueve A-Z y a-z, lo demás se queda igual
    resultado = []
    for caracter in texto:
        if "A" <= caracter <= "Z":
            base = ord("A")
        elif "a" <= caracter <= "z":
            base = ord("a")
        else:
            resultado.append(caracter)
            continue
        resultado.append(chr((ord(caracter) - base + desplazamiento) % 26 + base))
    return "".join(resultado)


def descifrar_cesar(texto, desplazamiento):
    return cesar(texto, -desplazamiento)


# 2. Palíndromos
SIN_ACENTOS = str.maketrans("áéíóúü", "aeiouu")


def es_palindromo(frase):
    # quito acentos, espacios y signos para comparar
    limpia = "".join(c for c in frase.lower().translate(SIN_ACENTOS) if c.isalnum())
    return limpia != "" and limpia == limpia[::-1]


# 3. Anagramas
def son_anagramas(palabra1, palabra2):
    a = palabra1.lower().replace(" ", "")
    b = palabra2.lower().replace(" ", "")
    return a != b and sorted(a) == sorted(b)


# 4. Contador de palabras
SIGNOS = ".,;:!?¡¿\"'()[]{}-—«»"


def palabras_frecuentes(parrafo, cantidad=5):
    texto = parrafo.lower()
    for signo in SIGNOS:
        texto = texto.replace(signo, " ")
    conteo = {}
    for palabra in texto.split():
        conteo[palabra] = conteo.get(palabra, 0) + 1
    # más veces primero, si empatan va alfabético
    return sorted(conteo.items(), key=lambda par: (-par[1], par[0]))[:cantidad]


# 5. Validador de IPv4
def es_ipv4(cadena):
    octetos = cadena.strip().split(".")
    if len(octetos) != 4:
        return False
    for octeto in octetos:
        try:
            valor = int(octeto)
        except ValueError:
            return False
        # así no paso cosas raras tipo 01 o +1
        if not 0 <= valor <= 255 or str(valor) != octeto:
            return False
    return True


# 6. Lectura segura
def leer_entero(mensaje, minimo, maximo):
    while True:
        texto = input(mensaje)
        try:
            numero = int(texto)
        except ValueError:
            print(f"'{texto.strip()}' no es un entero válido.")
        else:
            if minimo <= numero <= maximo:
                return numero
            print(f"El número debe estar entre {minimo} y {maximo}.")


# 7. Jerarquía de excepciones
def operacion_riesgosa(caso):
    try:
        if caso == 1:
            resultado = 10 / 0  # ZeroDivisionError
        elif caso == 2:
            resultado = math.exp(1000)  # OverflowError
        else:
            resultado = int("diez")  # ValueError
        print("Resultado:", resultado)
    # primero lo específico, Exception al final
    except ZeroDivisionError:
        print(f"Caso {caso}: ZeroDivisionError -> no se puede dividir entre cero.")
    except ArithmeticError as error:
        print(f"Caso {caso}: ArithmeticError ({type(error).__name__}) -> {error}")
    except Exception as error:
        print(f"Caso {caso}: Exception ({type(error).__name__}) -> {error}")


# 8. Relanzar
def obtener_precio(precios, producto):
    try:
        return precios[producto]
    except KeyError:
        print(f"[log] Producto no encontrado: {producto!r}")
        raise  # la vuelvo a lanzar para que la atrape main


# Pregunta de análisis: find() vs index()
def demostrar_find_index():
    texto = "Python Essentials"
    print(f"'{texto}'.find('Java') -> {texto.find('Java')}  (devuelve -1, no falla)")
    try:
        texto.index("Java")
    except ValueError as error:
        print(f"'{texto}'.index('Java') -> ValueError: {error}")


def main():
    titulo("1. Cifrado César")
    mensaje = "¡Hola, Mundo! Práctica ITLA 2026."
    cifrado = cesar(mensaje, 3)
    print("Original: ", mensaje)
    print("Cifrado:  ", cifrado)
    print("Descifrado:", descifrar_cesar(cifrado, 3))

    titulo("2. Palíndromos")
    for frase in ("Anita lava la tina", "Dábale arroz a la zorra el abad", "Python Essentials"):
        print(f"{frase!r}: {es_palindromo(frase)}")

    titulo("3. Anagramas")
    for a, b in (("Roma", "amor"), ("listen", "silent"), ("Python", "typhoon")):
        print(f"{a} / {b}: {son_anagramas(a, b)}")

    titulo("4. Las 5 palabras más frecuentes")
    parrafo = ("Python es un lenguaje sencillo. Python es potente, y Python es popular: "
               "en el ITLA se aprende Python, se practica Python y se disfruta el código. "
               "El código claro es el mejor código.")
    for palabra, veces in palabras_frecuentes(parrafo):
        print(f"{palabra:<10} {veces}")

    titulo("5. Validador de IPv4")
    for ip in ("192.168.1.1", "255.255.255.255", "256.1.1.1", "10.0.0", "a.b.c.d", "01.2.3.4", "1.2.3.-4"):
        print(f"{ip:<16} {es_ipv4(ip)}")

    titulo("6. Lectura segura")
    edad = leer_entero("Tu edad (0-120): ", 0, 120)
    print(f"Edad registrada: {edad}")

    titulo("7. Jerarquía de excepciones")
    for caso in (1, 2, 3):
        operacion_riesgosa(caso)

    titulo("8. Relanzar un KeyError")
    precios = {"cafe": 75, "pan": 25}
    print("Precio del pan:", obtener_precio(precios, "pan"))
    try:
        obtener_precio(precios, "jugo")
    except KeyError as error:
        print(f"main() recibió el KeyError relanzado: {error}")

    titulo("Análisis: find() vs index()")
    demostrar_find_index()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nEjecución interrumpida por el usuario.")
