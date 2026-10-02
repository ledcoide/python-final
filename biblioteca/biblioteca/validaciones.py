def validar_matricula(matricula):
    # formato AAAA-NNNN, tipo 2024-0153
    matricula = matricula.strip()
    partes = matricula.split("-")
    es_valida = (
        matricula.isascii()
        and len(partes) == 2
        and len(partes[0]) == 4 and partes[0].isdigit()
        and len(partes[1]) == 4 and partes[1].isdigit()
    )
    if not es_valida:
        raise ValueError(f"Matrícula inválida: '{matricula}'. Formato esperado AAAA-NNNN.")
    return matricula


def validar_isbn(isbn):
    limpio = isbn.strip().replace("-", "").replace(" ", "").upper()
    formato_ok = (
        limpio.isascii()
        and len(limpio) == 10
        and limpio[:9].isdigit()
        and (limpio[9].isdigit() or limpio[9] == "X")
    )
    if not formato_ok:
        raise ValueError(f"ISBN inválido: '{isbn.strip()}'. Debe tener 10 dígitos (el último puede ser X).")

    # dígito verificador: pesos 10, 9, ..., 1; X vale 10
    suma = 0
    for posicion, caracter in enumerate(limpio):
        valor = 10 if caracter == "X" else int(caracter)
        suma += valor * (10 - posicion)
    if suma % 11 != 0:
        raise ValueError(f"ISBN inválido: '{isbn.strip()}'. El dígito verificador no es correcto.")
    return limpio


def normalizar_nombre(nombre):
    nombre = " ".join(nombre.strip().split()).title()
    if not nombre:
        raise ValueError("El nombre no puede quedar vacío.")
    return nombre


def normalizar_titulo(titulo):
    titulo = " ".join(titulo.strip().split())
    if not titulo:
        raise ValueError("El título no puede quedar vacío.")
    return titulo


if __name__ == "__main__":
    print("Prueba rápida de validaciones.py")
    print(validar_matricula(" 2024-0153 "))
    print(validar_isbn("0-306-40615-2"))
    print(validar_isbn("080442957X"))
    print(normalizar_nombre("   maría   josé  PÉREZ "))
    for dato, funcion in [("2024-015", validar_matricula), ("0306406153", validar_isbn), ("   ", normalizar_nombre)]:
        try:
            funcion(dato)
        except ValueError as error:
            print("Error esperado ->", error)
