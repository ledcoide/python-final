VOCALES = "aeiouáéíóúü"


def contar_vocales(texto):
    return sum(1 for letra in texto.lower() if letra in VOCALES)


def invertir_texto(texto):
    return texto[::-1]


if __name__ == "__main__":
    print(f"__name__ = {__name__!r}  (ejecutado directamente)")
    print(contar_vocales("Murciélago"))
    print(invertir_texto("Python"))
