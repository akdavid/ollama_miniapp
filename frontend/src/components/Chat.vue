<template>
  <div class="chat">
    <h1>Chat avec Ollama</h1>
    <form @submit.prevent="sendMessage">
      <input
        v-model="userMessage"
        type="text"
        placeholder="Tapez votre message..."
        required
      />
      <button type="submit" :disabled="loading">Envoyer</button>
    </form>
    <div v-if="chatLog.length">
      <div v-for="(entry, index) in chatLog" :key="index" class="chat-entry">
        <p>
          <strong>{{ entry.role === 'user' ? 'Vous' : 'Assistant' }} :</strong>
          {{ entry.content }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userMessage: '',
      chatLog: [], // Historique des messages
      loading: false, // Indique si le message est en cours de traitement
    };
  },
  methods: {
    async sendMessage() {
      // Ajouter le message utilisateur au journal
      this.chatLog.push({ role: 'user', content: this.userMessage });

      // Préparer une nouvelle entrée vide pour la réponse en streaming
      const assistantEntry = { role: 'assistant', content: '' };
      this.chatLog.push(assistantEntry);

      this.loading = true;

      try {
        const response = await fetch('http://localhost:8000/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: this.userMessage }),
        });

        // Lire la réponse en mode streaming
        const reader = response.body.getReader();
        const decoder = new TextDecoder('utf-8');
        let done = false;

        while (!done) {
          const { value, done: readerDone } = await reader.read();
          done = readerDone;

          if (value) {
            const chunk = decoder.decode(value);
            // Ajouter le contenu reçu à la réponse en cours
            assistantEntry.content += chunk;
          }
        }
      } catch (error) {
        console.error("Erreur lors de l'envoi du message :", error);
        assistantEntry.content = 'Erreur de communication avec le serveur.';
      } finally {
        this.loading = false;
      }

      // Réinitialiser le champ de saisie
      this.userMessage = '';
    },
  },
};
</script>

<style>
.chat {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}
.chat-entry {
  margin-bottom: 10px;
}
input {
  width: 80%;
  padding: 10px;
  margin-right: 10px;
}
button {
  padding: 10px;
}
button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
