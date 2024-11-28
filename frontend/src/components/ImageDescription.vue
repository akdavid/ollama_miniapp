<template>
  <div class="image-description">
    <h1>Demander une description d'image</h1>
    <form @submit.prevent="sendImage">
      <label for="image-upload">Téléchargez une image :</label>
      <input
        type="file"
        id="image-upload"
        @change="handleFileChange"
        accept="image/*"
      />
      <button type="submit" :disabled="loading || !selectedImage">
        Envoyer
      </button>
    </form>

    <!-- Affichage de l'aperçu de l'image -->
    <div v-if="previewImage" class="image-preview">
      <h2>Aperçu de l'image :</h2>
      <img :src="previewImage" alt="Aperçu de l'image" />
    </div>

    <div v-if="loading" class="loading">Analyse de l'image en cours...</div>

    <div v-if="description" class="result">
      <h2>Description générée :</h2>
      <p>{{ description }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedImage: null,
      previewImage: null, // URL pour l'aperçu
      description: null,
      loading: false,
    };
  },
  methods: {
    handleFileChange(event) {
      this.selectedImage = event.target.files[0];

      // Générer l'aperçu de l'image sélectionnée
      if (this.selectedImage) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.previewImage = e.target.result;
        };
        reader.readAsDataURL(this.selectedImage);
      } else {
        this.previewImage = null;
      }
    },
    async sendImage() {
      if (!this.selectedImage) return;

      this.loading = true;
      this.description = null;

      const formData = new FormData();
      formData.append('image', this.selectedImage);

      try {
        const response = await fetch(
          'http://localhost:8000/api/image-description',
          {
            method: 'POST',
            body: formData,
          }
        );

        if (!response.ok) {
          throw new Error(`Erreur HTTP : ${response.status}`);
        }

        const data = await response.json();
        this.description = data.description;
      } catch (error) {
        console.error("Erreur lors de l'envoi de l'image :", error);
        this.description =
          "Une erreur s'est produite lors de l'analyse de l'image.";
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style>
.image-description {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}
.image-preview {
  margin-top: 20px;
  text-align: center;
}
.image-preview img {
  max-width: 100%;
  height: auto;
  border: 1px solid #ccc;
  border-radius: 8px;
  margin-top: 10px;
}
.loading {
  color: #007bff;
  font-weight: bold;
}
.result {
  margin-top: 20px;
}
</style>
