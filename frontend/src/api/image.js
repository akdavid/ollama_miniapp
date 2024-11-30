export async function fetchImageDescription(selectedImage) {
    const formData = new FormData();
    formData.append('image', selectedImage);

    try {
        const response = await fetch('http://localhost:8000/api/v1/image-description', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json();
        return data.description; // Returns the generated description
    } catch (error) {
        console.error('Error while sending the image:', error);
        throw new Error('An error occurred while analyzing the image.');
    }
}
