function generateAndDisplayImage(event) {
    event.preventDefault();
    const textInput = document.getElementById('text-input').value;
    const generatedImage = document.getElementById('generated-image');
    const loadingSpinner = document.getElementById('loading-spinner');
    const generateImageButton = document.getElementById('generate-image-button');
    
    // Hide the generated image and show the loading spinner
    generatedImage.style.display = "none";
    loadingSpinner.style.display = "block";
    generateImageButton.style.display = "none";
  
    // Send a POST request to generate the image
    fetch('http://54.145.236.113:443/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: textInput })
    })
    .then(response => response.text())
    .then(dataUri => {
      // Swap the loading spinner with the generated image
      generatedImage.onload = () => {
        loadingSpinner.style.display = "none";
        generatedImage.style.display = "block";
        generateImageButton.style.display = "block";
      };
      generatedImage.src = 'data:image/png;base64,' + dataUri;
    })
    .catch(error => console.error('Error generating image:', error));
  }
  
  document.querySelector('form').addEventListener('submit', generateAndDisplayImage);