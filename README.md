
# 🎧 Audio Course Transcriber & Rewriter

This application allows you to upload an audio file, transcribe it using Whisper, and then restructure the text into a clean, structured course format in HTML. It's designed to automatically transform spoken explanations into clear and interactive educational material.

---

## 🚀 Features

- Upload any audio file (all formats supported via `ffmpeg`)
- Automatic transcription using [OpenAI Whisper Turbo](https://github.com/openai/whisper)
- Automatic generation of:
  - ✅ Corrected transcript (spelling + interpretation fixes)
  - 📘 Structured course with examples
  - ❓ Multiple-choice questions to test comprehension
  - 🧾 Ready-to-use HTML output

---

## 🧰 Tech Stack

- **Frontend**: [Nuxt 3](https://nuxt.com) + Vue 3 + Pug
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) + Whisper model
- **Containerization**: Docker + Docker Compose
- **Languages**: TypeScript, Python

---

## 🗂 Project Structure

```
.
├── app.vue                 # Main Vue component
├── compose.yaml            # Docker Compose configuration
├── Dockerfile              # Frontend Dockerfile
├── Makefile                # Build/start commands
├── nuxt.config.ts          # Nuxt configuration
├── whisper/
│   ├── app.py              # FastAPI backend with Whisper
│   ├── Dockerfile          # Backend Dockerfile
│   └── requirements.txt    # Python dependencies
```

---

## ⚙️ Installation & Usage

### 1. Clone the repository

```bash
git clone <project-url>
cd <project-directory>
```

### 2. Build Docker images

```bash
make build
```

### 3. Start the app

```bash
make start
```

- Frontend available at: [http://localhost:9090](http://localhost:9090)
- Backend endpoint: [http://localhost:8000/transcribe/](http://localhost:8000/transcribe/)

---

## 📦 Main Dependencies

### Frontend

- `nuxt`
- `vue`
- `vue-router`
- `@nuxtjs/google-fonts`
- `pug`

### Backend

- `fastapi`
- `uvicorn`
- `openai-whisper`
- `python-multipart`
- `ffmpeg` (via apt in Docker)

---

## 📄 License

MIT License — free to use, modify, and distribute.
