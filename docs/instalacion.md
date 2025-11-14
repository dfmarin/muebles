# Instalación

## Prerrequisitos

* Tener instalado un entorno Linux o WSL (Windows Subsystem for Linux) en tu sistema.
* Tener instalado **Python 3.12+** (o la versión que el proyecto requiera).
* Tener instalado `git` para clonar el repositorio.
* Tener instalado `pip` (o `pip3`) para instalar las dependencias.

## Paso 1: Clonar el repositorio

Abre tu terminal en Linux/WSL y ejecuta:

```bash
git clone https://github.com/dfmarin/muebles.git
cd muebles
```

Esto crea la carpeta `muebles` con el contenido del repositorio.

## Paso 2: Crear un entorno virtual (altamente recomendado)

Para evitar conflictos con otras instalaciones de Python, se recomienda crear un entorno virtual. Puedes usar `venv`:

```bash
python3 -m venv venv
# Activar el entorno virtual:
source venv/bin/activate
```

Verás que tu prompt cambia (por ejemplo, con `(venv)` al inicio). Mientras esté activo, cualquier instalación de paquetes se hará dentro del entorno.

## Paso 3: Instalar las dependencias

Dentro del repositorio (y con el entorno virtual activado), ejecuta:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Esto instalará todos los paquetes listados en `requirements.txt`.

## Paso 4: Ejecutar el proyecto de ejemplo

Una vez instaladas las dependencias, puedes ejecutar el script principal. En este repositorio, el ejemplo de uso está al final del archivo principal (ver README). Probablemente el comando sea:

```bash
python3 main.py
```

O bien, si el archivo se llama diferente (revisa en la raíz del proyecto). Esto mostrará el inventario, realizará una venta, etc., según el ejemplo incluido.

## Paso 5: (Opcional) Generar la documentación con MkDocs

El repositorio menciona que es un proyecto de ejemplo de documentación automática con MkDocs. Para generarla y verla localmente, puedes hacer lo siguiente:

1. Instala MkDocs si aún no lo hiciste (puede estar en `requirements.txt` o instalarlo aparte):

   ```bash
   pip install mkdocs mkdocs-material
   ```

2. Dentro de la carpeta del proyecto, ejecuta:

   ```bash
   mkdocs serve
   ```

   Esto iniciará un servidor local, normalmente en `http://127.0.0.1:8000/`, donde podrás ver la documentación generada.

3. Para construir la documentación para producción:

   ```bash
   mkdocs build
   ```

   Esto generará la carpeta `site/` con los archivos HTML listos para publicar.

## Paso 6: Limpieza y buenas prácticas

* Cuando termines de trabajar, puedes salir del entorno virtual con:

  ```bash
  deactivate
  ```

* Si ya no necesitas el entorno virtual, puedes eliminar la carpeta `venv`.

* Es buena práctica añadir un archivo `.gitignore` que ya está en el repositorio, para excluir la carpeta `venv` y otros archivos no deseados.

## Problemas comunes y tips

* Si al ejecutar `python3` o `pip` te lanza un error de versión, verifica que la versión de Python sea 3.x. Puedes comprobar con:

  ```bash
  python3 --version
  ```

* Si `pip install -r requirements.txt` falla por permisos, asegúrate de estar dentro del entorno virtual o añade `--user` si fuera necesario (aunque usar el entorno virtual es más limpio).

* Si en `mkdocs serve` el puerto 8000 ya está ocupado, puedes especificar otro puerto así:

  ```bash
  mkdocs serve -a 127.0.0.1:8080
  ```

---

## Resumen rápido de comandos

```bash
# Clonar
git clone https://github.com/dfmarin/muebles.git
cd muebles

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Ejecutar el programa
python3 main.py    # o según el nombre del archivo principal

# Generar documentación (opcional)
mkdocs serve
# y para producción:
mkdocs build

# Cuando termines:
deactivate
```

