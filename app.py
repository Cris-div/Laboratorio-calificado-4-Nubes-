from flask import Flask, request, render_template_string, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Descargador de videos</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            padding: 50px;
            background: #f4f4f4;
        }
        .container {
            background: white;
            max-width: 600px;
            margin: auto;
            padding: 30px;
            border-radius: 10px;
        }
        input {
            width: 90%;
            padding: 12px;
            margin: 15px 0;
        }
        button {
            padding: 12px 25px;
            background: #028090;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📥 Descargador de videos</h1>
        <p>YouTube, Instagram, TikTok, Facebook y LinkedIn</p>

        <form method="POST">
            <input type="text" name="url"
                   placeholder="Ingresa la URL del video"
                   required>
            <br>
            <button type="submit">Descargar video</button>
        </form>

        {% if mensaje %}
            <p>{{ mensaje }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():

    mensaje = ""

    if request.method == "POST":

        url = request.form.get("url")

        try:
            nombre = str(uuid.uuid4())

            opciones = {
                "outtmpl": f"{DOWNLOAD_FOLDER}/{nombre}.%(ext)s",
                # Se prioriza AVC/H.264 con audio M4A: es el formato MP4 más
                # compatible con el reproductor predeterminado de Windows.
                "format": "bestvideo[vcodec^=avc][ext=mp4]+bestaudio[ext=m4a]/best[vcodec^=avc][ext=mp4]/best",
                "merge_output_format": "mp4",
                "noplaylist": True,
                # YouTube requiere un runtime de JavaScript para resolver sus desafíos.
                # Node.js se instala en las imágenes Docker del proyecto.
                "js_runtimes": {"node": {}},
            }

            with yt_dlp.YoutubeDL(opciones) as ydl:
                info = ydl.extract_info(url, download=True)
                archivo = ydl.prepare_filename(info)

            return send_file(
                archivo,
                as_attachment=True,
                download_name=os.path.basename(archivo)
            )

        except Exception as e:
            mensaje = "No se pudo descargar el video. Verifica que la URL sea válida."

    return render_template_string(HTML, mensaje=mensaje)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
