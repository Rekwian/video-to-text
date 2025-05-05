from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware  # Importation de CORSMiddleware
import whisper
import tempfile
import subprocess
import os

app = FastAPI()

# Autorisation de CORS pour tous les domaines (tu peux restreindre à des domaines spécifiques)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Liste des domaines autorisés, "*" autorise tous les domaines
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Autorise tous les en-têtes
)

model = whisper.load_model("turbo")

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    # Créer deux fichiers temporaires : 1 pour l'original, 1 pour l'audio MP3
    with tempfile.NamedTemporaryFile(delete=False) as input_tmp, \
        tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as output_tmp:
        
        # Sauvegarde du fichier uploadé
        input_tmp.write(await file.read())
        input_tmp.flush()

        # Extraction audio en MP3 via ffmpeg
        command = [
            "ffmpeg",
            "-y",  # overwrite si besoin
            "-i", input_tmp.name,
            "-vn",  # pas de vidéo
            "-acodec", "libmp3lame",
            "-ar", "44100",
            "-ac", "2",
            output_tmp.name
        ]
        subprocess.run(command, check=True)

        # Transcription avec Whisper Turbo
        result = model.transcribe(output_tmp.name)

    # Nettoyage des fichiers temporaires
    os.unlink(input_tmp.name)
    os.unlink(output_tmp.name)

    return {"text": result["text"]}
