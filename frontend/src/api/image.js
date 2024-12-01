export async function fetchImageDescription(selectedImage, customPrompt) {
    const formData = new FormData();
    formData.append('image', selectedImage);
    formData.append('prompt', customPrompt);

    try {
        const response = await fetch('http://localhost:8000/api/v1/image-description', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json();
        return data.description;
    } catch (error) {
        console.error('Error while sending the image:', error);
        throw new Error('An error occurred while analyzing the image.');
    }
}
