import platform
from biblioteca import __version__, inventario
from biblioteca.validaciones import validar_matricula
import biblioteca.utilidades as util

MENU = f"""
=== BIBLIOTECA ITLA v{__version__} ===
1. Registrar estudiante
2. Agregar material
3. Prestar material
4. Devolver material
5. Buscar por palabra clave
6. Reporte de inventario
7. Salir"""


def mensaje_de(error):
    # KeyError imprime con comillas, así que saco el texto de args
    return error.args[0] if error.args else type(error).__name__


def leer_entero(mensaje, minimo=0):
    while True:
        texto = input(mensaje).strip()
        try:
            numero = int(texto)
        except ValueError:
            print(f"[Error] '{texto}' no es un número entero.")
        else:
            if numero >= minimo:
                return numero
            print(f"[Error] El número debe ser mayor o igual que {minimo}.")


def mostrar_sistema():
    print(f"Sistema operativo: {platform.system()} {platform.release()}")
    print(f"Python: {platform.python_version()}")


def opcion_registrar():
    matricula = validar_matricula(input("Matrícula: "))
    nombre = inventario.registrar_estudiante(matricula, input("Nombre completo: "))
    print(f"Estudiante {nombre} ({matricula}) registrado.")


def opcion_agregar():
    titulo = input("Título: ")
    tipo = input(f"Tipo ({', '.join(inventario.DIAS_PRESTAMO)}): ")
    isbn = input("ISBN-10 (Enter si no aplica): ")
    codigo = inventario.agregar_material(titulo, tipo, isbn)
    datos = inventario.materiales[codigo]
    print(f"Material agregado con código {codigo} ({datos['tipo']}, "
          f"{inventario.DIAS_PRESTAMO[datos['tipo']]} día(s) de préstamo).")


def opcion_prestar():
    matricula = validar_matricula(input("Matrícula: "))
    inventario.obtener_estudiante(matricula)  # si no existe, salta al except del menú
    codigo = input("Código del material: ")
    codigo_prestamo, dias = inventario.prestar(matricula, codigo)
    print(f"Préstamo {codigo_prestamo} registrado. Devolver en {dias} días.")


def opcion_devolver():
    matricula = validar_matricula(input("Matrícula: "))
    inventario.obtener_estudiante(matricula)
    codigo = input("Código del material: ").strip().upper()
    inventario.obtener_material(codigo)
    dias = leer_entero("Días transcurridos desde el préstamo: ")
    codigo_prestamo, retraso = inventario.devolver(matricula, codigo, dias)
    print(f"Préstamo {codigo_prestamo} cerrado. Material {codigo} devuelto.")
    if retraso:
        print(f"Retraso: {retraso} día(s) = {util.dias_a_semanas(retraso)} semana(s) de penalización.")
    else:
        print("Devuelto a tiempo, sin penalización.")


def opcion_buscar():
    resultados = inventario.buscar(input("Palabra clave: "))
    if not resultados:
        print("No se encontraron materiales con esa palabra.")
    for codigo, datos in resultados:
        print(inventario.formatear_material(codigo, datos))


# cada número del menú apunta a su función
ACCIONES = {
    "1": opcion_registrar,
    "2": opcion_agregar,
    "3": opcion_prestar,
    "4": opcion_devolver,
    "5": opcion_buscar,
    "6": inventario.reporte,
}


def ejecutar_menu():
    respuesta = input("¿Cargar datos de ejemplo? (s/n) [s]: ").strip().lower()
    if respuesta in ("", "s", "si", "sí"):
        inventario.cargar_datos_demo()
        print("Datos de ejemplo cargados (opción 6 para verlos).")

    while True:
        print(MENU)
        opcion = input("Opción: ").strip()
        if opcion == "7":
            break
        accion = ACCIONES.get(opcion)
        if accion is None:
            print(f"[Error] Opción inválida: '{opcion}'. Elige un número del 1 al 7.")
            continue
        try:
            accion()
        except (KeyError, ValueError) as error:
            print(f"[Error] {mensaje_de(error)}")
        except Exception as error:
            # por si se cuela algo que no esperaba
            print(f"[Error inesperado] {type(error).__name__}: {mensaje_de(error)}")


def main():
    mostrar_sistema()
    try:
        ejecutar_menu()
    except (KeyboardInterrupt, EOFError):
        print("\nEntrada interrumpida por el usuario.")
    finally:
        print("Sesión finalizada. ¡Hasta pronto!")


if __name__ == "__main__":
    main()
