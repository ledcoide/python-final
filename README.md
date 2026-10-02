# Práctica Final: Python Essentials 2 (Módulos 1 y 2)

**Estudiante:** _Nombre Apellido_
**Matrícula:** _AAAA-NNNN_
**Sección:** _____
**Instituto Tecnológico de Las Américas (ITLA)**

## Estructura

```
Apellido_Nombre_PracticaFinal/
├── biblioteca/          Proyecto integrador (ver biblioteca/README.md)
│   ├── main.py
│   ├── README.md
│   └── biblioteca/
│       ├── __init__.py
│       ├── inventario.py
│       ├── validaciones.py
│       └── utilidades.py
├── ejercicios/
│   ├── herramientas/    Paquete propio: conversiones.py y textos.py
│   ├── modulo1.py       Parte 1: módulos, paquetes y PIP
│   └── modulo2.py       Parte 2: strings, listas y excepciones
└── README.md
```

## Cómo ejecutar

Se necesita Python 3.10 o superior. Todo usa solo la biblioteca estándar, excepto el ejercicio 6 de la Parte 1, que usa `colorama`.

```bash
# Proyecto integrador
cd biblioteca
python main.py

# Ejercicios (desde la carpeta ejercicios/)
cd ejercicios
python modulo1.py
python modulo2.py
```

`modulo1.py` pide el radio del círculo. `modulo2.py` pide una edad para el ejercicio de lectura segura. El resto de los ejercicios se ejecuta con datos de ejemplo.

## PIP (Parte 1, ejercicio 6)

Comando usado para instalar el paquete (dentro de un entorno virtual):

```bash
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
python -m pip install colorama
```

Salida de `pip show colorama`:

```
Name: colorama
Version: 0.4.6
Summary: Cross-platform colored terminal text.
Home-page: https://github.com/tartley/colorama
Author:
Author-email: Jonathan Hartley <tartley@tartley.com>
License:
Location: .../.venv/lib/python3.14/site-packages
Requires:
Required-by:
```

Si `colorama` no está instalado, `modulo1.py` no falla: muestra el comando para instalarlo.

## Preguntas de análisis

### 1. ¿Qué pasa si ejecutas un módulo directamente frente a importarlo?

Cuando Python ejecuta un archivo directamente (`python modulo1.py`), le asigna `__name__ = "__main__"`. Cuando el archivo se importa, `__name__` toma el nombre del módulo (`"modulo1"`, `"herramientas.conversiones"`).

En los dos casos se ejecuta todo el código del nivel superior del archivo. Lo que cambia es el bloque `if __name__ == "__main__":`, que solo se ejecuta cuando el archivo se lanza directamente. Así un módulo puede traer su propia prueba o programa principal sin que ese código corra cada vez que otro archivo lo importa.

Demostración (`modulo1.py` imprime su `__name__` al cargarse):

```
$ python modulo1.py
[modulo1] cargado con __name__ = '__main__'
...                                   <- main() se ejecuta

$ python -c "import modulo1"
[modulo1] cargado con __name__ = 'modulo1'
                                      <- main() NO se ejecuta
```

### 2. ¿Cuál es la diferencia entre `find()` e `index()` cuando la subcadena no existe?

Si la subcadena existe, los dos métodos devuelven la misma posición. Si no existe:

- `find()` devuelve `-1` y no lanza ninguna excepción.
- `index()` lanza `ValueError: substring not found`.

`find()` sirve cuando no encontrar la subcadena es algo normal y basta con comparar el resultado con `-1`. `index()` sirve cuando la subcadena *debería* estar, y su ausencia es un error que conviene manejar con `try/except`. Las listas solo tienen `index()`, que también lanza `ValueError`. La demostración está al final de `modulo2.py`.
