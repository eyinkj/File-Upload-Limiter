# File Size Limiter Microservice

This microservice allows you to check the size of PDF and DOCX files before uploading them. It ensures that the files are under 5MB in size.

## Communication Contract

### Requesting Data

To request data from the microservice, send a `POST` request to the `/check-file-size` endpoint with the file included in the form data.


**Request Example (using JavaScript's fetch API):**

```javascript
async function checkFileSize(file) {
  const url = 'https://file-size-limiter-67005a553eac.herokuapp.com/check-file-size';
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await fetch(url, {
      method: 'POST',
      body: formData,
    });

    const result = await response.json();
    console.log(result);
  } catch (error) {
    console.error('Error:', error);
  }
}

// Usage example
const file = document.querySelector('input[type="file"]').files[0];
checkFileSize(file);
