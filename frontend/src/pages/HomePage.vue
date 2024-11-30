<template>
    <DefaultLayout>
        <!-- Hero Section -->
        <section class="hero-section">
            <div class="hero-content">
                <h1>Welcome to Ollama MiniApp</h1>
                <p>
                    Unlock the power of advanced Language and Vision models with an intuitive and
                    modern interface.
                </p>
                <div class="hero-buttons">
                    <a href="/chat" class="btn-primary">Start Chatting</a>
                    <a href="/image-description" class="btn-secondary">Describe an Image</a>
                </div>
            </div>
        </section>

        <!-- Features Section -->
        <section class="features-section">
            <div class="features-content">
                <h2>Explore the Features</h2>
                <div class="features-grid">
                    <!-- Feature 1 -->
                    <div class="feature-card">
                        <h3>Chat with LLM</h3>
                        <p>
                            Engage in real-time conversations with advanced language models like
                            Llama and Mistral.
                        </p>
                        <a href="/chat" class="btn-primary">Learn More</a>
                    </div>

                    <!-- Feature 2 -->
                    <div class="feature-card">
                        <h3>Image Description</h3>
                        <p>
                            Upload images to generate detailed descriptions using Vision-Language
                            Models.
                        </p>
                        <a href="/image-description" class="btn-secondary">Learn More</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Backend Test (For Developers Only) -->
        <section class="backend-test">
            <p class="developer-note">
                This feature is intended for developers to test backend connectivity.
            </p>
            <button @click="testBackend">Test Backend Connection</button>
            <p v-if="message" :class="messageClass">{{ message }}</p>
        </section>
    </DefaultLayout>
</template>

<script>
import { testBackendConnection } from '@/api/index';
import DefaultLayout from '../layouts/DefaultLayout.vue';

export default {
    components: { DefaultLayout },
    data() {
        return {
            message: '', // Holds the response message or error
        };
    },
    computed: {
        messageClass() {
            return this.message.includes('Success') ? 'success' : 'error';
        },
    },
    methods: {
        async testBackend() {
            try {
                const response = await testBackendConnection();
                this.message = `Success: ${response.message}`;
            } catch (error) {
                this.message = 'Error: Unable to connect to the backend.';
            }
        },
    },
};
</script>

<style>
/* Hero Section */
.hero-section {
    background: linear-gradient(90deg, #007bff, #0056b3);
    color: white;
    text-align: center;
    padding: 4rem 1rem;
}

.hero-content h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    font-weight: bold;
}

.hero-content p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
}

.hero-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
}

.hero-buttons a {
    padding: 0.8rem 1.5rem;
    border-radius: 5px;
    text-decoration: none;
    font-size: 1rem;
    font-weight: bold;
    transition: transform 0.3s;
}

.hero-buttons .btn-primary {
    background: white;
    color: #007bff;
}

.hero-buttons .btn-primary:hover {
    transform: scale(1.05);
    background: #e6e6e6;
}

.hero-buttons .btn-secondary {
    background: #28a745;
    color: white;
}

.hero-buttons .btn-secondary:hover {
    transform: scale(1.05);
}

/* Features Section */
.features-section {
    padding: 4rem 1rem;
    background: #f8f9fa;
}

.features-content h2 {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 2rem;
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
}

.feature-card {
    background: white;
    border-radius: 10px;
    padding: 2rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.3s, box-shadow 0.3s;
}

.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
}

.feature-card h3 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
    color: #343a40;
}

.feature-card p {
    font-size: 1rem;
    margin-bottom: 1.5rem;
    color: #6c757d;
}

/* Backend Test */
.backend-test {
    text-align: center;
    margin: 2rem 0;
}

.backend-test .developer-note {
    font-size: 0.9rem;
    color: #6c757d;
    margin-bottom: 0.5rem;
}

.backend-test button {
    background: transparent;
    border: none;
    color: #007bff;
    text-decoration: underline;
    font-size: 0.9rem;
    cursor: pointer;
}

.backend-test button:hover {
    color: #0056b3;
}

.backend-test .success {
    color: #28a745;
    margin-top: 0.5rem;
}

.backend-test .error {
    color: #dc3545;
    margin-top: 0.5rem;
}
</style>
