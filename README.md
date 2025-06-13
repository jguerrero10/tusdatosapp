# Mis Eventos - Plataforma de Gestión de Eventos

Este proyecto es una solución completa para la gestión de eventos desarrollada como parte de una prueba técnica para el rol de Desarrollador Python. La solución incluye un backend desarrollado en FastAPI y un frontend desarrollado en Vue.js, orquestados mediante Docker Compose.

## Estructura del Proyecto

```text
.
├── backend/       # API REST con FastAPI y PostgreSQL
├── frontend/      # Interfaz de usuario con Vue.js
├── docker-compose.yml
└── test_main.http # Archivo de pruebas de endpoints
```

## Descripción General

La aplicación permite:
- Crear, editar y listar eventos con capacidad y sesiones. 
- Registrar usuarios y autenticarse.
- Registrar asistentes a eventos (con control de capacidad). 
- Acceder a una interfaz para visualizar y gestionar eventos.

## 🧰 Tecnologías Utilizadas

### Backend
- Python 3.12 
- FastAPI 
- PostgreSQL 
- SQLAlchemy + SQLModel 
- Alembic (migraciones)
- Poetry (gestión de dependencias)
- Pytest (tests)
- Docker

### Frontend
- Vue.js 
- Vue Router 
- Pinia o similar (gestión de estado)
- Axios (consumo de API)
- Vite (compilación)
- Docker + Nginx

## ⚙️ Instalación y Ejecución
### Requisitos Previos
- Docker y Docker Compose instalados.
- Node.js y npm instalados (para el frontend).

### Pasos
1. Clona el repositorio:
    ```bash
    git clone https://github.com/jguerrero10/tusdatosapp.git
    cd mis-eventos
    ```
2. Editar y/o copiar el archivo `.env.example` a `.env` en el directorio `backend/` y ajustar las variables de entorno según sea necesario.
3. Levantar el entorno completo:
    ```bash
    docker-compose up --build
    ```
4. Acceder al backend en `http://localhost:8000` y al frontend en `http://localhost:5173`.

## Funcionalidades clave

### Backend
- CRUD de eventos con búsqueda por nombre 
- Registro/login con JWT 
- Protección de rutas 
- Gestión de sesiones y ponentes 
- Control de capacidad

### Frontend
- Formulario de creación/edición (usuarios logueados)
- Autenticación (login/registro)
- Perfil de usuario con eventos registrados

