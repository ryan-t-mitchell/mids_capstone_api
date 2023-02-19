  function generateAndDisplayImage(event) {
    const textInput = document.getElementById('text-input').value;
  
    // // fetch('http://localhost:8000/generate', {
    // // fetch('http://18.207.245.10:8000/generate', {
    // // This new IP will use port 443 (HTTPS) by default. Open 443 on EC2 instance.
    // // This IP is also elastic, so it should remain the same even after restarting EC2 instance. 
    // // fetch('https://54.145.236.113/generate', {
    fetch('http://54.145.236.113:443/generate', {    
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: textInput })
    //   agent: new https.Agent({
    //     rejectUnauthorized: false
    //   })
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
  }
  
  document.querySelector('form').addEventListener('submit', generateAndDisplayImage);