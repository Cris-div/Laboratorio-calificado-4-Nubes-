FROM node:22-slim AS node_runtime

FROM python:3.11-slim

LABEL maintainer="tu-email@ejemplo.com"
LABEL description="Descargador de videos de redes sociales"

WORKDIR /app

# yt-dlp usa Node.js para resolver los desafíos de JavaScript de YouTube.
COPY --from=node_runtime /usr/local/bin/node /usr/local/bin/node
RUN apt-get update \
    && apt-get install --yes --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/* \
    && node --version \
    && ffmpeg -version

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN mkdir -p downloads

EXPOSE 5000

CMD ["python", "app.py"]
