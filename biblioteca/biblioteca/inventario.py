from biblioteca import utilidades, validaciones

MAX_PRESTAMOS = 3
DIAS_PRESTAMO = {"Libro": 14, "Revista": 3, "Laptop": 1}

# codigo -> titulo, tipo, disponible, isbn, prestamo
materiales = {}
# matricula -> nombre y lista de códigos prestados
estudiantes = {}


def obtener_estudiante(matricula):
    if matricula not in estudiantes:
        raise KeyError(f"No existe un estudiante con la matrícula {matricula}.")
    return estudiantes[matricula]


def obtener_material(codigo):
    if codigo not in materiales:
        raise KeyError(f"No existe un material con el código {codigo}.")
    return materiales[codigo]


def registrar_estudiante(matricula, nombre):
    matricula = validaciones.validar_matricula(matricula)
    nombre = validaciones.normalizar_nombre(nombre)
    if matricula in estudiantes:
        raise ValueError(f"La matrícula {matricula} ya está registrada.")
    estudiantes[matricula] = {"nombre": nombre, "prestamos": []}
    return nombre


def agregar_material(titulo, tipo, isbn=""):
    titulo = validaciones.normalizar_titulo(titulo)
    tipo = tipo.strip().title()
    if tipo not in DIAS_PRESTAMO:
        raise ValueError(f"Tipo inválido: '{tipo}'. Opciones: {', '.join(DIAS_PRESTAMO)}.")
    isbn = validaciones.validar_isbn(isbn) if isbn.strip() else ""

    codigo = utilidades.codificar_titulo(titulo)
    if codigo in materiales:
        raise ValueError(f"Ya existe un material con el código {codigo} ('{materiales[codigo]['titulo']}').")
    materiales[codigo] = {
        "titulo": titulo,
        "tipo": tipo,
        "disponible": True,
        "isbn": isbn,
        "prestamo": None,
    }
    return codigo


def prestar(matricula, codigo):
    matricula = validaciones.validar_matricula(matricula)
    codigo = codigo.strip().upper()
    estudiante = obtener_estudiante(matricula)
    material = obtener_material(codigo)

    if not material["disponible"]:
        raise ValueError(f"El material {codigo} ('{material['titulo']}') no está disponible.")
    if len(estudiante["prestamos"]) >= MAX_PRESTAMOS:
        raise ValueError(
            f"{estudiante['nombre']} ya tiene {MAX_PRESTAMOS} préstamos activos (límite alcanzado)."
        )

    usados = [datos["prestamo"] for datos in materiales.values() if datos["prestamo"]]
    codigo_prestamo = utilidades.generar_codigo_prestamo(usados)
    estudiante["prestamos"].append(codigo)
    material["disponible"] = False
    material["prestamo"] = codigo_prestamo

    assert len(estudiante["prestamos"]) <= MAX_PRESTAMOS
    return codigo_prestamo, DIAS_PRESTAMO[material["tipo"]]


def devolver(matricula, codigo, dias_transcurridos):
    matricula = validaciones.validar_matricula(matricula)
    codigo = codigo.strip().upper()
    estudiante = obtener_estudiante(matricula)
    material = obtener_material(codigo)
    if dias_transcurridos < 0:
        raise ValueError("Los días transcurridos no pueden ser negativos.")

    # index lanza ValueError si ese material no está en su lista
    try:
        estudiante["prestamos"].index(codigo)
    except ValueError:
        raise ValueError(f"{estudiante['nombre']} no tiene prestado el material {codigo}.") from None

    estudiante["prestamos"].remove(codigo)
    codigo_prestamo = material["prestamo"]
    material["disponible"] = True
    material["prestamo"] = None
    retraso = max(0, dias_transcurridos - DIAS_PRESTAMO[material["tipo"]])
    return codigo_prestamo, retraso


def buscar(palabra_clave):
    clave = palabra_clave.strip().lower()
    if not clave:
        raise ValueError("La palabra clave no puede estar vacía.")
    encontrados = [
        (codigo, datos) for codigo, datos in materiales.items()
        if datos["titulo"].lower().find(clave) != -1
    ]
    return sorted(encontrados, key=lambda par: par[1]["titulo"].lower())


def formatear_material(codigo, datos):
    # si el título es muy largo lo recorto
    titulo = datos["titulo"] if len(datos["titulo"]) <= 32 else datos["titulo"][:29] + "..."
    estado = "Disponible" if datos["disponible"] else f"Prestado ({datos['prestamo']})"
    return f"{codigo:<9} {titulo:<32} {datos['tipo']:<8} {estado}"


def reporte():
    print("\n--- Inventario (ordenado por título) ---")
    if not materiales:
        print("(sin materiales registrados)")
    else:
        print(f"{'Código':<9} {'Título':<32} {'Tipo':<8} Estado")
        for codigo, datos in sorted(materiales.items(), key=lambda par: par[1]["titulo"].lower()):
            print(formatear_material(codigo, datos))
        disponibles = len([datos for datos in materiales.values() if datos["disponible"]])
        print(f"Total: {len(materiales)} material(es), {disponibles} disponible(s).")

    print("\n--- Estudiantes ---")
    if not estudiantes:
        print("(sin estudiantes registrados)")
    for matricula, datos in sorted(estudiantes.items()):
        prestados = ", ".join(datos["prestamos"]) or "ninguno"
        print(f"{matricula}  {datos['nombre']:<24} {len(datos['prestamos'])}/{MAX_PRESTAMOS} préstamos: {prestados}")


def cargar_datos_demo():
    registrar_estudiante("2024-0153", "ana martínez")
    registrar_estudiante("2023-0871", "luis  pérez")
    agregar_material("Python Essentials", "Libro", "0306406152")
    agregar_material("El Lenguaje de Programación C", "Libro", "0131103628")
    agregar_material("Redes Cisco CCNA", "Libro", "080442957X")
    agregar_material("National Geographic Octubre", "Revista")
    agregar_material("Laptop Dell Latitude 5420", "Laptop")


if __name__ == "__main__":
    print("Prueba rápida de inventario.py")
    cargar_datos_demo()
    print("Préstamo:", prestar("2024-0153", "pyt-725"))
    print("Búsqueda 'python':", [codigo for codigo, _ in buscar("PYTHON")])
    for accion in (lambda: prestar("2024-0153", "PYT-725"), lambda: prestar("2099-0000", "PYT-725")):
        try:
            accion()
        except (KeyError, ValueError) as error:
            print("Error esperado ->", error.args[0])
    print("Devolución (20 días):", devolver("2024-0153", "PYT-725", 20))
    reporte()
