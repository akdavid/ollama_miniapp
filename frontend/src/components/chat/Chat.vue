<template>
    <div class="chat-container">
        <!-- Title -->
        <h1 class="chat-title">Chat with Ollama</h1>

        <!-- Model Selector -->
        <div class="model-selector">
            <label for="model-select" class="model-label">Choose a model:</label>
            <select v-model="selectedModel" id="model-select" class="model-dropdown" required>
                <option v-for="model in llmModels" :key="model" :value="model">
                    {{ model }}
                </option>
            </select>
        </div>

        <!-- Chat Log -->
        <div class="chat-log">
            <div
                v-for="(entry, index) in chatLog"
                :key="index"
                class="chat-entry"
                :class="{
                    'user-entry': entry.role === 'user',
                    'assistant-entry': entry.role === 'assistant',
                }"
            >
                <p class="chat-message">{{ entry.content }}</p>
            </div>
        </div>

        <!-- Message Input -->
        <form @submit.prevent="sendMessage" class="input-form">
            <div class="input-container">
                <input
                    v-model="userMessage"
                    type="text"
                    class="chat-input"
                    placeholder="Type your message..."
                    required
                />
                <button type="submit" class="send-button" :disabled="loading">
                    {{ loading ? 'Sending...' : 'Send' }}
                </button>
            </div>
        </form>
    </div>
</template>

<script>
import { fetchChatResponse } from '@/api/chat';
import { fetchLLMModels } from '@/api/models';

export default {
    data() {
        return {
            userMessage: '',
            chatLog: [],
            loading: false,
            llmModels: [], // List of available models
            selectedModel: '', // Model selected by the user
        };
    },
    async created() {
        await this.loadLLMModels(); // Fetch available models on component load
    },
    methods: {
        async loadLLMModels() {
            try {
                this.llmModels = await fetchLLMModels(); // Fetch models from the backend
                if (this.llmModels.length > 0) {
                    this.selectedModel = this.llmModels[0]; // Automatically select the first model
                }
            } catch (error) {
                console.error('Error fetching LLM models:', error);
            }
        },
        async sendMessage() {
            if (!this.selectedModel) {
                alert('Please select a model before sending a message.');
                return;
            }

            this.chatLog.push({ role: 'user', content: this.userMessage });
            const assistantEntry = { role: 'assistant', content: '' };
            this.chatLog.push(assistantEntry);

            this.loading = true;

            try {
                await fetchChatResponse(this.userMessage, this.selectedModel, chunk => {
                    assistantEntry.content += chunk;
                    this.$forceUpdate(); // Update the UI as chunks are received
                });
            } catch (error) {
                console.error('Error communicating with the server:', error);
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
/* General Container */
.chat-container {
    max-width: 800px;
    margin: 2rem auto;
    display: flex;
    flex-direction: column;
    height: 80vh; /* Adjust for responsive design */
    border: 1px solid #dee2e6;
    border-radius: 10px;
    background-color: #ffffff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Title */
.chat-title {
    font-size: 2rem;
    font-weight: bold;
    color: #343a40;
    text-align: center;
    padding: 1rem;
    border-bottom: 1px solid #dee2e6;
}

/* Model Selector */
.model-selector {
    padding: 1rem;
    border-bottom: 1px solid #dee2e6;
    background-color: #f8f9fa;
}

.model-label {
    font-size: 1rem;
    font-weight: 600;
    color: #495057;
    margin-right: 1rem;
}

.model-dropdown {
    padding: 0.8rem;
    font-size: 1rem;
    border: 1px solid #ced4da;
    border-radius: 5px;
    background-color: #ffffff;
    color: #495057;
}

.model-dropdown:focus {
    border-color: #80bdff;
    outline: none;
    box-shadow: 0 0 4px rgba(0, 123, 255, 0.5);
}

/* Chat Log */
.chat-log {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
    background-color: #f8f9fa;
}

.chat-entry {
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.user-entry {
    align-items: flex-end;
    text-align: right;
}

.assistant-entry {
    align-items: flex-start;
    text-align: left;
}

.chat-message {
    display: inline-block;
    padding: 0.8rem;
    border-radius: 10px;
    font-size: 1rem;
    word-wrap: break-word;
    max-width: 75%;
}

.user-entry .chat-message {
    background-color: #d1e7ff;
    color: #495057;
}

.assistant-entry .chat-message {
    background-color: #e9ecef;
    color: #495057;
}

/* Input Form */
.input-form {
    padding: 1rem;
    border-top: 1px solid #dee2e6;
    background-color: #ffffff;
}

.input-container {
    display: flex;
    gap: 1rem;
}

.chat-input {
    flex: 1;
    padding: 0.8rem;
    font-size: 1rem;
    border: 1px solid #ced4da;
    border-radius: 5px;
}

.chat-input:focus {
    border-color: #80bdff;
    outline: none;
    box-shadow: 0 0 4px rgba(0, 123, 255, 0.5);
}

.send-button {
    padding: 0.8rem 1.5rem;
    font-size: 1rem;
    font-weight: bold;
    color: #ffffff;
    background-color: #007bff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.send-button:hover {
    background-color: #0056b3;
}

.send-button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
}
</style>
