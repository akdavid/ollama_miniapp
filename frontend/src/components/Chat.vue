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
      // Add user message to chat log
      this.chatLog.push({ role: 'user', content: this.userMessage });

      // Add an empty assistant entry to append chunks
      const assistantEntry = { role: 'assistant', content: '' };
      this.chatLog.push(assistantEntry);

      this.loadimodelng = true;

      try {
        // Send the message using the streaming chat route
        const response = await fetch('http://localhost:8000/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: this.userMessage }),
        });

        if (!response.ok) {
          throw new Error(`HTTP error: ${response.status}`);
        }

        // Process the response stream
        const reader = response.body.getReader();
        const decoder = new TextDecoder('utf-8');
        let done = false;

        while (!done) {
          const { value, done: readerDone } = await reader.read();
          done = readerDone;

          if (value) {
            // Decode the chunk
            const chunk = decoder.decode(value);

            // Log the received chunk in the browser console
            console.log('Chunk received:', chunk);

            // Append the chunk to the assistant's response
            assistantEntry.content += chunk;
            this.$forceUpdate(); // Manually trigger UI re-render if necessary
          }
        }
      } catch (error) {
        console.error('Error while sending the message:', error);
        assistantEntry.content = 'Error communicating with the server.';
      } finally {
        this.loading = false;
        this.userMessage = ''; // Clear the input field
      }
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
