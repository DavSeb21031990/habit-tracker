uvi# Configuración Inicial
## Configurar entorno virtual con `venv`
### Crear y activar entorno virtual
```python title="Crear entorno virtual .venv"
python -m venv .venv
```
```python title="Activar entorno .venv"
source .venv/bin/activate
```

### Instalar dependencias
- FastAPI:
  - Es un framework web para Python moderno y rápido, diseñado para crear APIs (interfaces de programación de aplicaciones).
- Uvicorn:
  - Es un servidor web ligero y rápido.
  - Soporta concurrencia.
- Pydantic:
  - Es una librería de Python que se usa para validar y manejar datos mediante modelos basados en anotaciones de tipo.
- Pytest:
  - Es un framework de testing para Python.
  - Sirve para crear y ejecutar pruebas automatizadas de tu código, de forma simple y potente.
```python title="Instalaciones"
pip install --upgrade pip
pip install fastapi uvicorn[standard] pydantic pytest
```

### Crear archivo `requirements.txt`
- `pip freeze`: Obtiene todas las dependencias instaladas en el entorno virtual.
- `> <file>`: Redirige la salida del comando `pip freeze` hacia un archivo.
```python title="Crear archivo requirements.txt"
pip freeze > requirements.txt
```

## Estructura de arquitectura limpia
```bash
app/
  domain/               # Entidades del dominio (p. ej. Habit)
  application/          # Casos de uso/servicios de aplicación
  infrastructure/       # Adaptadores: DB, repos, mappers
  interfaces/           # Entradas/salidas: HTTP (FastAPI routers)
tests/
```

# Iniciar Servidor
- Inicia el servidor `uvicorn`
```bash
uvicorn app.main:app --reload --port 8000
```