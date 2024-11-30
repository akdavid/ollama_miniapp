const API_BASE_URL = 'http://localhost:8000/api/v1';

/**
 * Fetches the list of available models from the backend.
 * @returns {Promise<string[]>} A list of models.
 */
export const fetchModels = async () => {
    try {
        const response = await fetch(`${API_BASE_URL}/models`);
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }
        const data = await response.json();
        return data.models || [];
    } catch (error) {
        console.error('Error while fetching models:', error);
        throw error;
    }
};

/**
 * Sends a user message to the selected model and returns a streaming response.
 * @param {string} prompt - The user's message.
 * @param {string} model - The selected model.
 * @param {function} onChunkReceived - Callback function for each chunk of data received.
 */
export const fetchChatResponse = async (prompt, model, onChunkReceived) => {
    try {
        const response = await fetch(`${API_BASE_URL}/chat?model=${model}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt }),
        });

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
                if (onChunkReceived) {
                    onChunkReceived(chunk);
                }
            }
        }
    } catch (error) {
        console.error('Error while communicating with the server:', error);
        throw error;
    }
};
