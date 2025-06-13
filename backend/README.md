# 🎯 Event Management API - Backend

Este es el backend del sistema de gestión de eventos, desarrollado con **FastAPI** y arquitectura hexagonal. Incluye autenticación JWT, manejo de usuarios, eventos, ponentes y control de capacidad con PostgreSQL y migraciones gestionadas por Alembic.

---

## 🚀 Tecnologías

- 🐍 Python 3.12
- ⚡ FastAPI
- 🧱 SQLModel (sobre SQLAlchemy)
- 🐘 PostgreSQL
- 📦 Poetry
- 📜 Alembic
- 🔒 JWT (con `jose`)
- 🧪 Pytest + coverage
- 🐳 Docker + Docker Compose
---


## ⚙️ Instalación local

### Copia el archivo `.env`
```bash
cp .env.example .env
```
> Modifica los valores necesarios.

### Levanta el entorno con Docker

```bash
docker-compose up --build
```

Esto hace lo siguiente:
- Inicia PostgreSQL 
- Espera a que la base esté disponible 
- Ejecuta migraciones automáticamente 
- Inicia FastAPI en http://localhost:8000

### Endpoints

Visita la documentación automática: http://localhost:8000/docs


## Pruebas

Para ejecutar las pruebas, asegúrate de tener el entorno levantado y ejecuta:

```bash
poetry run pytest --cov
```

## Pre-commit hooks
Instala los hooks de pre-commit para asegurar calidad de código:

```bash
pre-commit install
pre-commit run --all-files
```

## Coverage

Para generar un reporte de cobertura, ejecuta:

```bash
poetry run pytest --cov-report html --cov
```
Esto generará un reporte en `htmlcov/index.html` que puedes abrir en tu navegador.

```text
========================================================================================================== tests coverage ==========================================================================================================
_________________________________________________________________________________________ coverage: platform linux, python 3.12.3-final-0 __________________________________________________________________________________________

Name                                          Stmts   Miss  Cover   Missing
---------------------------------------------------------------------------
adapters/web/api/__init__.py                      0      0   100%
adapters/web/api/auth.py                         32      0   100%
adapters/web/api/events.py                       62      0   100%
adapters/web/api/speaker.py                      10      0   100%
core/__init__.py                                  0      0   100%
core/entities/__init__.py                         0      0   100%
core/entities/event.py                           22      0   100%
core/entities/registration.py                     6      0   100%
core/entities/user.py                            16      0   100%
core/ports/__init__.py                            0      0   100%
core/ports/repositories/__init__.py               0      0   100%
core/ports/repositories/event_repository.py       4      0   100%
core/security/__init__.py                         0      0   100%
core/security/auth.py                            14      0   100%
core/security/dependencies.py                    22      0   100%
---------------------------------------------------------------------------
TOTAL                                           188      0   100%

```