<template>
  <div class="chat-container">
    <h1 class="chat-title">Chat avec Ollama</h1>
    <form @submit.prevent="sendMessage" class="chat-form">
      <div class="model-selector">
        <label for="model-select" class="model-label"
          >Choisir un modèle :</label
        >
        <select
          v-model="selectedModel"
          id="model-select"
          class="model-dropdown"
          required
        >
          <option v-for="model in models" :key="model" :value="model">
            {{ model }}
          </option>
        </select>
      </div>
      <div class="input-container">
        <input
          v-model="userMessage"
          type="text"
          class="chat-input"
          placeholder="Tapez votre message..."
          required
        />
        <button type="submit" class="send-button" :disabled="loading">
          {{ loading ? 'Envoi...' : 'Envoyer' }}
        </button>
      </div>
    </form>
    <div v-if="chatLog.length" class="chat-log">
      <div
        v-for="(entry, index) in chatLog"
        :key="index"
        class="chat-entry"
        :class="{
          'user-entry': entry.role === 'user',
          'assistant-entry': entry.role === 'assistant',
        }"
      >
        <p class="chat-message">
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
      chatLog: [],
      loading: false,
      models: [], // Liste des modèles disponibles
      selectedModel: '', // Modèle sélectionné par l'utilisateur
    };
  },
  created() {
    this.fetchModels(); // Récupérer les modèles au chargement du composant
  },
  methods: {
    async fetchModels() {
      try {
        const response = await fetch('http://localhost:8000/api/models');
        if (!response.ok) {
          throw new Error(`HTTP error: ${response.status}`);
        }
        const data = await response.json();
        this.models = data.models;
        this.selectedModel = this.models[0]; // Sélectionnez le premier modèle par défaut
      } catch (error) {
        console.error('Error fetching models:', error);
      }
    },
    async sendMessage() {
      this.chatLog.push({ role: 'user', content: this.userMessage });
      const assistantEntry = { role: 'assistant', content: '' };
      this.chatLog.push(assistantEntry);

      this.loading = true;

      try {
        const response = await fetch(
          `http://localhost:8000/api/chat?model=${this.selectedModel}`,
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: this.userMessage }),
          }
        );

        if (!response.ok) {
          throw new Error(`HTTP error: ${response.status}`);
        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder('utf-8');
        let done = false;

        while (!done) {
          const { value, done: readerDone } = await reader.read();
          done = readerDone;

          if (value) {
            const chunk = decoder.decode(value);
            assistantEntry.content += chunk;
            this.$forceUpdate();
          }
        }
      } catch (error) {
        console.error('Error while sending the message:', error);
        assistantEntry.content = 'Error communicating with the server.';
      } finally {
        this.loading = false;
        this.userMessage = '';
      }
    },
  },
};
</script>

<style>
/* Container */
.chat-container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 1.5rem;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  font-family: 'Arial', sans-serif;
}

/* Title */
.chat-title {
  font-size: 1.8rem;
  color: #333;
  text-align: center;
  margin-bottom: 1.5rem;
}

/* Form */
.chat-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* Model Selector */
.model-selector {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.model-label {
  font-weight: bold;
  color: #555;
}
.model-dropdown {
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
}

/* Input and Button */
.input-container {
  display: flex;
  gap: 0.5rem;
}
.chat-input {
  flex: 1;
  padding: 0.8rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.send-button {
  padding: 0.8rem 1.5rem;
  font-size: 1rem;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}
.send-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
.send-button:hover:not(:disabled) {
  background-color: #0056b3;
}

/* Chat Log */
.chat-log {
  margin-top: 2rem;
  padding: 1rem;
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 5px;
  overflow-y: auto;
  max-height: 300px;
}

/* Chat Entries */
.chat-entry {
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
}
.user-entry {
  align-items: flex-end;
  text-align: right;
}
.assistant-entry {
  align-items: flex-start;
  text-align: left;
}
.user-entry .chat-message {
  background: #d1e7ff;
  color: #333;
  padding: 0.5rem 1rem;
  border-radius: 10px;
  max-width: 70%;
  margin-left: auto;
}
.assistant-entry .chat-message {
  background: #f5f5f5;
  color: #333;
  padding: 0.5rem 1rem;
  border-radius: 10px;
  max-width: 70%;
}

/* Message Content */
.chat-message {
  font-size: 1rem;
  word-wrap: break-word;
}
</style>
