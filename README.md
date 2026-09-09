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