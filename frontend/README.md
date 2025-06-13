# tusdatosappfrontend

Este frontend está construido con Vue 3 + Vite + Pinia + Vue Router + Tailwind CSS. Permite gestionar eventos mediante una interfaz tipo dashboard conectada a un backend FastAPI.

## Scripts disponibles

Para iniciar el proyecto, puedes usar los siguientes comandos:

```bash
npm install
```

Corre la aplicación en modo desarrollo:

```bash
npm run dev
```

Compila para producción:

```bash
npm run build
```

## Variables de entorno

Crea un archivo `.env` en la raíz del proyecto y define las siguientes variables:

```env
VITE_API_URL=http://localhost:8000
```


## Docker

Para construir y correr el frontend en un contenedor Docker, asegúrate de tener Docker instalado y ejecuta:

```bash
docker build -t eventos-frontend -f Dockerfile .
```

Ejecución:

```bash
docker run -p 5173:80 eventos-frontend
```
> Por defecto sirve la app compilada desde /dist usando nginx.

## Acceso a la aplicación
Abre tu navegador y visita:

```http request
http://localhost:5173
```

## Estructura del proyecto

```text
├── Dockerfile
├── index.html
├── jsconfig.json
├── nginx.conf
├── package.json
├── package-lock.json
├── public
│   └── favicon.ico
├── README.md
├── src
│   ├── api
│   ├── api.js
│   ├── App.vue
│   ├── assets
│   ├── components
│   ├── main.js
│   ├── router
│   ├── store
│   └── views
└── vite.config.js

```

## Funcionalidades

- Autenticación de usuarios (login/registro)
- CRUD completo de eventos (crear, listar, editar, inactivar)
- Vista de eventos registrados por el usuario 
- Estilo responsive con Tailwind 
- Navegación protegida según login 
- Diseño tipo dashboard

