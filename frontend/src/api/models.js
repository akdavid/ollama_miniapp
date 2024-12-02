const API_BASE_URL = 'http://localhost:8000/api/v1';

/**
 * Fetches the available models (LLM and VLM) from the backend.
 * @returns {Promise<{ llm_models: string[], vlm_model: string }>} The available models.
 */
export const fetchModels = async () => {
    try {
        const response = await fetch(`${API_BASE_URL}/models`);
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }
        const data = await response.json();
        return data; // { llm_models: [...], vlm_model: "model_name" }
    } catch (error) {
        console.error('Error while fetching models:', error);
        throw error;
    }
};

/**
 * Returns the available LLM models.
 * @returns {Promise<string[]>} A list of LLM models.
 */
export const fetchLLMModels = async () => {
    const models = await fetchModels();
    return models.llm_models;
};

/**
 * Returns the current VLM model.
 * @returns {Promise<string>} The VLM model.
 */
export const fetchVLMModel = async () => {
    const models = await fetchModels();
    return models.vlm_model;
};
