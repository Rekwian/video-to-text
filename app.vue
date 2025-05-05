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
const transcript = ref(`Alors maintenant qu'on a vu comment est-ce qu'on pouvait utiliser des fonctions qui avaient été créées par PHP, on va voir comment est-ce qu'on peut créer nos propres fonctions pour nos propres besoins. Alors pour nommer une fonction, on va avoir les mêmes règles que les variables sans le dollar, et petite surprise, on n'a pas de distinction entre une fonction et une procédure. On va la déclarer de la même façon, la seule différence c'est qu'il y en a une qui au final retournera quelque chose, et l'autre ne retournera rien. Enfin, petite chose aussi à savoir, c'est que les fonctions n'ont pas besoin d'avoir été définies avant leur utilisation, le tout c'est que la fonction existe bien et qu'ils puissent la trouver pour pouvoir l'appeler. Alors comment est-ce qu'on va faire pour créer une fonction ? Pour créer une fonction, on va utiliser le mot-clé function, on va lui donner un nom, on va indiquer les paramètres qu'elle prend, éventuellement le type de retour si sa fonction retourne quelque chose, si ce n'est pas une procédure, et enfin on va pouvoir donc, entre une paire d'accolades, indiquer ce qu'elle fait, et si nécessaire, on terminera par return et la valeur qu'elle doit retourner. De nos jours, en PHP, on va avoir tendance à donner du type à nos arguments, ce qui n'était pas le cas à l'origine. Le fait de typer nos paramètres, ici on a, pareil dans cet exemple, typer $valeur1 et $valeur2 tous les deux en tant que valeur de type float, et on a indiqué qu'elle retournait un type float, ça va permettre de vérifier est-ce qu'on appelle bien cette fonction avec les beaux paramètres. Le fait d'avoir fait le déclare strict type égal à 1, va indiquer qu'on ne veut pas qu'il y ait de conversion implicite qui soit effectuée entre différents types. Donc si par exemple, on attendait une valeur booléenne, et puis qu'on donnait un tableau vide, il aurait pu dire, ça c'est équivalent à false. Voilà, moi j'ai dit non, je ne veux pas ça, et donc généralement, on va plutôt interdire ce comportement-là. La seule petite conversion implicite qui va être acceptée, c'est quand on demande une valeur de type nombre réel, float, comme dans cet exemple, et que je lui donne une valeur entière. Donc là ici, je vais donner par exemple 82 et la valeur 35, donc l'une sous forme d'une variable, l'autre sous forme d'un littéral. Et là, pas de problème, là il accepte effectivement de faire cette conversion implicite, puisque un entier est un cas particulier de nombre réel. Donc pour appeler la fonction, j'ai juste indiqué son nom, entre parenthèses, les valeurs qu'elle attend, et en retour, je récupère donc la valeur qui a été calculée par ma fonction.`);
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
* N'hesite pas a mettre symbole/emoji afin d'illustrer ta réecriture.`)

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
