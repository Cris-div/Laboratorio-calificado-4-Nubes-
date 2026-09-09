# 📥 Descargador de Videos con Docker

## Descripción

Aplicación web desarrollada con Python y Flask que permite ingresar la URL de un video para realizar su descarga.

La aplicación utiliza la herramienta `yt-dlp` y está preparada para trabajar con contenido público de diferentes plataformas, como:

- YouTube
- Instagram
- TikTok
- Facebook
- LinkedIn

El proyecto fue desarrollado y posteriormente containerizado utilizando Docker.

> Úsalo únicamente para contenido público cuya descarga estés autorizado a realizar. Respeta los términos de uso y los derechos de autor de cada plataforma.

---

## Tecnologías utilizadas

- Python 3.11
- Flask 3.0.0
- yt-dlp
- Docker
- Docker Desktop

---

## Estructura del proyecto

```text
sem04-caso1/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Dockerfile.optimizado
├── Dockerfile.multistage
├── .dockerignore
└── README.md
```

---

## Pasos de instalación y ejecución

### Requisitos previos

Para ejecutar el proyecto con Docker, instala y abre [Docker Desktop](https://www.docker.com/products/docker-desktop/). Verifica que Docker esté funcionando con:

```bash
docker --version
```

Si se ejecutará sin Docker, se requiere Python 3.11 o una versión compatible y `pip`.

### 1. Obtener el proyecto

Clona el repositorio (reemplaza la URL por la del repositorio correspondiente) o descarga el código fuente. Luego entra a la carpeta del proyecto:

```bash
git clone <URL_DEL_REPOSITORIO>
cd sem04-caso1
```

### 2. Construir la imagen Docker

Desde la raíz del proyecto, construye la imagen usando el `Dockerfile` principal:

```bash
docker build -t descargador-videos .
```

También se incluyen dos variantes de construcción. Para usarlas, especifica el archivo con `-f`:

```bash
# Imagen basada en una versión optimizada
docker build -t descargador-videos:optimizado -f Dockerfile.optimizado .

# Imagen con construcción en múltiples etapas
docker build -t descargador-videos:multistage -f Dockerfile.multistage .
```

### 3. Ejecutar el contenedor

Inicia la aplicación y publica el puerto 5000 del contenedor en el puerto 5000 de tu equipo:

```bash
docker run --name descargador-videos -p 5000:5000 descargador-videos
```

Mientras este comando esté en ejecución, abre en el navegador:

```text
http://localhost:5000
```

Ingresa una URL válida, presiona **Descargar video** y el navegador iniciará la descarga cuando el proceso termine.

Para ejecutar el contenedor en segundo plano, usa:

```bash
docker run -d --name descargador-videos -p 5000:5000 descargador-videos
```

Para detenerlo posteriormente:

```bash
docker stop descargador-videos
```

Si el contenedor ya existe y se desea volver a iniciarlo, utiliza:

```bash
docker start descargador-videos
```

### Ejecución local sin Docker (opcional)

1. Crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   ```

   En Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   En macOS o Linux:

   ```bash
   source .venv/bin/activate
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Inicia la aplicación:

   ```bash
   python app.py
   ```

4. Visita `http://localhost:5000` en el navegador.

---

## Solución de problemas

- **El puerto 5000 ya está en uso:** cambia el primer puerto del parámetro `-p`, por ejemplo: `docker run -p 8080:5000 descargador-videos`. Después visita `http://localhost:8080`.
- **Docker no responde:** confirma que Docker Desktop esté abierto y que el motor de Docker se encuentre iniciado.
- **No se descarga el video:** revisa que la URL sea pública, válida y que la plataforma permita el acceso mediante `yt-dlp`.
