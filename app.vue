<template lang="pug">
.container
  form.form(@submit.prevent="extract")
    .form-wrapper
      .file-input-container
        label.file-label(for='file') Télécharge ton fichier audio
        input#file.file-input(type='file' name='file')
        button.submit-btn(type='submit' :disabled='loading')
          span.loading-spinner(v-if='loading') Chargement...
          span(v-else) Extraire
    .row
      .transcript-container
        h2 Transcription :
        pre(v-if='loading') Chargement...
        pre.transcript-text {{ transcript }}
      .transcript-container
        h2 Prompt :
        pre(v-if='loading') Chargement...
        pre.transcript-text(v-if='transcript') {{ prompt }}
</template>

<script setup>
const transcript = ref(``);
const loading = ref(false);
const prompt = computed(() => `Ce texte provient de Whisper :

${transcript.value}

1. Correction :
Corrige uniquement les fautes d'orthographe et d'interprétation, met des retours à la ligne pour le rendre plus lisible. Retourne cette version corrigée en premier.

2. Réécriture :
Ensuite, réécris ce texte sous forme d'un cours structuré :

* Clarifie les explications tout en conservant le contenu et le sens original.
* Ajoute des exemples pour illustrer les points clés.
* Crée 5 questions à choix multiples pour évaluer la compréhension, basées sur le contenu.

3. Format :
Retourne le tout au format HTML, prêt à intégrer (sans balise <body>).

* La première partie doit afficher le texte corrigé tel quel.
* La seconde partie doit afficher la version structurée du cours, avec les exemples et les questions.
* Place les réponses des questions dans une balise <details> à la fin.

Règles à respecter :

* La réponse doit être uniquement en français.
* La réponse doit être uniquement en HTML.
* Les réponses doivent être justifier brievement.
* Le contenu doit rester fidèle au texte original.
* N'hesite pas a mettre symbole/emoji afin d'illustrer ta réecriture.
* Ne lance pas d'analyse.
* Ne fait pas de canvas.`)

async function extract(event) {
  transcript.value = '';
  loading.value = true;
  if (transcript.value) { 
    loading.value = false;
    return;
  }
  try {
    const response = await $fetch('http://localhost:8000/transcribe/', {
      method: 'POST',
      body: new FormData(event.target)
    });
  
    transcript.value = response.text;
    loading.value = false;
  } catch (e) {
    console.error(e);
  } finally {
    loading.value = false;
  }
}
</script>

<style>
:root {
  --color-background: #f0f0f0;
  --color-background-text: #1a1a1a;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-background: #1a1a1a;
    --color-background-text: #f0f0f0;
}
}

body {
  background-color: var(--color-background);
  color: var(--color-background-text);
  padding: 0;
  margin: 0;
  min-width: 100vw;
  min-height: 100vh;
}
.container {
  margin: 0 auto;
  padding: 20px;
  font-family: 'Candara', sans-serif;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-wrapper {
  display: flex;
  gap: 20px;
  justify-content: center;

  button {
    width: max-content;
  }
}
.file-input-container {
  align-items: center;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.file-label {
  font-size: 1.6rem;
  font-weight: bold;
  color: var(--color-background-text);
}

.file-input {
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.row {
  display: flex;
  gap: 10px;
}

.submit-btn {
  background-color: #f6ac3c;
  color: white;
  border: none;
  padding: 15px;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  display: flex;
  align-items: center;
}

.submit-btn:hover {
  background-color: #45a049;
}

.loading-spinner {
  margin-right: 10px;
}

.transcript-container {
  background-color: var(--color-background);
  border: 2px solid var(--color-background-text);
  border-radius: 1.6rem;
  display: flex;
  flex-direction: column;
  gap: 20px;
  font-size: 1rem;
  flex: 1;
  padding: 15px;
  overflow-wrap: break-word;
  word-wrap: break-word;
  white-space: pre-wrap;
}

.transcript-text {
  white-space: pre-line;
  font-family: 'Work Sans', sans-serif;
  color: var(--color-background-text);
}

h2 {
  color: var(--color-background-text);
  font-size: 18px;
  margin-bottom: 10px;
}

</style>
