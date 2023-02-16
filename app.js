function generateAndDisplayImage(event) {
    const textInput = document.getElementById('text-input').value;
  
    fetch('http://localhost:8000/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: textInput })
    })
    .then(response => response.text())
    .then(dataUri => {
      const image = new Image();
      image.onload = () => {
        document.getElementById('generated-image').src = 'data:image/png;base64,' + dataUri;
      };
      image.src = 'data:image/png;base64,' + dataUri;
    })
    .catch(error => console.error('Error generating image:', error));
  
    event.preventDefault();
  }
  
  document.querySelector('form').addEventListener('submit', generateAndDisplayImage);
  