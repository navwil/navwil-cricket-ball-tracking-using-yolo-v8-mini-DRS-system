const videoUpload = document.getElementById('videoUpload');
const processButton = document.getElementById('processButton');
const showTrackedButton = document.getElementById('showTrackedButton');
const output = document.getElementById('output');
const resultImage = document.getElementById('resultImage');

videoUpload.addEventListener('change', function() {
  // Enable buttons when a video is uploaded
  processButton.disabled = false;
  showTrackedButton.disabled = false;
  processButton.style.opacity = 1;
});

// Function to display processing message
function displayProcessingMessage() {
  output.innerHTML = 'Processing video...';
}

// Function to display processing complete message
function displayProcessingCompleteMessage() {
  output.innerHTML = '<b>Video processing complete!</b><br>Ball trajectory analysis available.';
  showTrackedButton.style.display = 'block'; // Show "See Tracked Video" button after processing
}

// Function to send video to server for processing
function processVideo() {
  // Create FormData object to send the video file
  const formData = new FormData();
  formData.append('file', videoUpload.files[0]);

  // Send POST request to server
  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/', true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        // Display processing complete message after receiving response
        displayProcessingCompleteMessage();
      } else {
        // Handle error
        output.innerHTML = 'Error processing video.';
      }
    }
  };
  xhr.send(formData);
}

// Process video when "Start Tracking" button is clicked
processButton.addEventListener('click', function() {
  displayProcessingMessage(); // Display processing message immediately
  processVideo(); // Send video to server for processing
});

// Display tracked image when "See Result" button is clicked
showTrackedButton.addEventListener('click', function() {
  // Show the result image
  resultImage.style.display = 'block';
  // Set the source of the result image
  resultImage.src = 'C:\Users\navee\OneDrive\Desktop\mini using yolo\static\script.js';
});
