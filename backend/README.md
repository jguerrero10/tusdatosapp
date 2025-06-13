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