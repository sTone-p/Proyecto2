---Proyecto Curso Python+FastAPI N° 2---

PROYECTO = Gestor de Entradas y Salidas

~~ Requisitos ~~

*Python 3.10 o superior
*GIT 
*Pip (Para instalar Requirements)

==================== Instalación ====================

1) # Clonar el repositorio con GIT

2) # Crear el entorno virtual (VENV)
-> python -m venv venv
   -> .\venv\Scripts\activate (Windows)

3) # Instalación de Dependencias
-> pip install -r requirements.txt     - Para producción
   -> pip install -r requierements-dev.txt     - Para desarrollo


==================== Levantar Servidor ====================

1) # Con FastAPI

fastapi dev src/app.py     ! Requiere tener instalado FastAPI

2) # Uvicorn

uvicorn src.app:api_server --reload

3) # Python

main.py





