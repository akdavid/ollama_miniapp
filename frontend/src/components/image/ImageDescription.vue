<template>
    <div class="image-description-container">
        <!-- Title -->
        <h1 class="title">Request an Image Description</h1>

        <!-- Form -->
        <form @submit.prevent="processImage" class="form">
            <div class="form-group">
                <label for="image-upload" class="label">Upload an image:</label>
                <input
                    type="file"
                    id="image-upload"
                    class="input-file"
                    @change="handleFileChange"
                    accept="image/*"
                />
            </div>

            <!-- Settings Button -->
            <div class="settings-toggle">
                <button type="button" class="btn-settings" @click="togglePromptInput">⚙️</button>
            </div>

            <!-- Conditional Prompt Input -->
            <div v-if="showPromptInput" class="form-group">
                <label for="custom-prompt" class="label">Custom Prompt:</label>
                <input
                    type="text"
                    id="custom-prompt"
                    v-model="customPrompt"
                    placeholder="Write your custom prompt here"
                    class="input-prompt"
                />
            </div>

            <button type="submit" class="btn-submit" :disabled="loading || !selectedImage">
                {{ loading ? 'Analyzing...' : 'Submit' }}
            </button>
        </form>

        <!-- Image Preview -->
        <div v-if="previewImage" class="image-preview">
            <h2 class="preview-title">Image Preview:</h2>
            <img :src="previewImage" alt="Preview of the uploaded image" class="preview-image" />
        </div>

        <!-- Loading Indicator -->
        <div v-if="loading" class="loading">Analyzing the image...</div>

        <!-- Result -->
        <div v-if="description" class="result">
            <h2 class="result-title">Generated Description:</h2>
            <p class="result-text">{{ description }}</p>
        </div>
    </div>
</template>

<script>
import { fetchImageDescription } from '@/api/image';

export default {
    data() {
        return {
            selectedImage: null,
            previewImage: null,
            description: null,
            loading: false,
            customPrompt: "What's in this image?", // Default prompt
            showPromptInput: false, // Toggle for showing/hiding prompt input
        };
    },
    methods: {
        handleFileChange(event) {
            this.selectedImage = event.target.files[0];

            if (this.selectedImage) {
                const reader = new FileReader();
                reader.onload = e => {
                    this.previewImage = e.target.result;
                };
                reader.readAsDataURL(this.selectedImage);
            } else {
                this.previewImage = null;
            }
        },
        async processImage() {
            if (!this.selectedImage) return;

            this.loading = true;
            this.description = null;

            try {
                this.description = await fetchImageDescription(
                    this.selectedImage,
                    this.customPrompt,
                );
            } catch (error) {
                this.description = 'An error occurred while analyzing the image.';
                console.error(error);
            } finally {
                this.loading = false;
            }
        },
        togglePromptInput() {
            this.showPromptInput = !this.showPromptInput;
        },
    },
};
</script>

<style>
/* Container */
.image-description-container {
    max-width: 700px;
    margin: 2rem auto;
    padding: 2rem;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    font-family: 'Arial', sans-serif;
    color: #333;
}

/* Title */
.title {
    text-align: center;
    font-size: 2rem;
    font-weight: bold;
    color: #343a40;
    margin-bottom: 1.5rem;
}

/* Form */
.form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.form-group {
    display: flex;
    flex-direction: column;
}

.label {
    font-size: 1rem;
    font-weight: 600;
    color: #495057;
    margin-bottom: 0.5rem;
}

.input-file {
    padding: 0.8rem;
    font-size: 1rem;
    border: 1px solid #ced4da;
    border-radius: 5px;
    background-color: #f8f9fa;
}

.input-file:focus {
    border-color: #80bdff;
    outline: none;
    box-shadow: 0 0 4px rgba(0, 123, 255, 0.5);
}

.input-prompt {
    padding: 0.8rem;
    font-size: 1rem;
    border: 1px solid #ced4da;
    border-radius: 5px;
    background-color: #f8f9fa;
}

.input-prompt:focus {
    border-color: #80bdff;
    outline: none;
    box-shadow: 0 0 4px rgba(0, 123, 255, 0.5);
}

.btn-submit {
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

.btn-submit:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
}

.btn-submit:not(:disabled):hover {
    background-color: #0056b3;
}

/* Settings Button */
.btn-settings {
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
    font-weight: bold;
    color: #333;
    background-color: #f1f1f1;
    border: 1px solid #ccc;
    border-radius: 5px;
    cursor: pointer;
    align-self: flex-start;
    transition: background-color 0.3s ease;
}

.btn-settings:hover {
    background-color: #e6e6e6;
}

/* Image Preview */
.image-preview {
    margin-top: 1.5rem;
    text-align: center;
}

.preview-title {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #495057;
}

.preview-image {
    max-width: 100%;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Loading Indicator */
.loading {
    margin-top: 1.5rem;
    text-align: center;
    font-size: 1.1rem;
    font-weight: bold;
    color: #007bff;
}

/* Result Section */
.result {
    margin-top: 2rem;
}

.result-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #28a745;
    margin-bottom: 1rem;
}

.result-text {
    font-size: 1rem;
    line-height: 1.5;
    color: #495057;
}
</style>
