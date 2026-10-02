# Biblioteca ITLA v1.0

Aplicación de consola para gestionar préstamos de una biblioteca. Usa solo funciones, listas y diccionarios, y solo la biblioteca estándar de Python (3.10 o superior).

## Ejecutar

```bash
cd biblioteca
python main.py
```

Al iniciar, el programa muestra el sistema operativo y la versión de Python, y pregunta si quieres cargar datos de ejemplo. Los datos de ejemplo son los estudiantes `2024-0153` y `2023-0871` y cinco materiales; por ejemplo, `PYT-725` es *Python Essentials*.

## Pruebas rápidas de cada módulo

Cada módulo tiene su bloque `if __name__ == "__main__":`. Se ejecutan como módulos del paquete desde esta carpeta:

```bash
python -m biblioteca.validaciones
python -m biblioteca.utilidades
python -m biblioteca.inventario
```

## Estructura

| Archivo | Contenido |
|---|---|
| `main.py` | Menú y manejo de errores. Importa de tres formas: `import platform`, `from biblioteca import inventario` e `import biblioteca.utilidades as util` |
| `biblioteca/__init__.py` | `__version__ = "1.0"` |
| `biblioteca/validaciones.py` | Valida la matrícula (AAAA-NNNN) y el ISBN-10 (dígito verificador módulo 11), y normaliza nombres y títulos |
| `biblioteca/utilidades.py` | Código de préstamo `PR-NNNN` (con `random`), código de catálogo `ABC-NNN` (con `ord`) y paso de días a semanas (con `math.ceil`) |
| `biblioteca/inventario.py` | Diccionarios de materiales y estudiantes: préstamo, devolución, búsqueda y reporte. Lanza `KeyError` y `ValueError` |

## Reglas

- Días de préstamo: Libro 14, Revista 3, Laptop 1. Están en el diccionario `DIAS_PRESTAMO`, sin un `if` por tipo.
- Un estudiante puede tener como máximo 3 préstamos activos. Un `assert` interno comprueba esa regla.
- En la devolución, los días de retraso se convierten a semanas de penalización con `math.ceil`.
- El código de catálogo se genera a partir del título. Por eso, dos materiales con el mismo título tendrían el mismo código, y el segundo se rechaza.
- Ninguna entrada cierra el programa con un traceback: los errores se muestran como `[Error] ...`. Si se pulsa Ctrl+C o se cierra la entrada, el programa termina de forma ordenada.
