import { fetchChatResponse } from './chat';
import { fetchImageDescription } from './image';

export { fetchChatResponse, fetchImageDescription };

export const testBackendConnection = async () => {
    try {
        const response = await fetch('http://localhost:8000/api/v1/test');
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('Error testing backend connection:', error);
        throw error;
    }
};
