# File Size Limiter Microservice

This microservice allows you to check the size of PDF and DOCX files before uploading them. It ensures that the files are under 5MB in size.

## Communication Contract

### Requesting Data

To request data from the microservice, send a `POST` request to the `/check-file-size` endpoint with the file included in the form data.

**Endpoint:**
**Request Example (using Python's `requests` library):**

```python
import requests

url = 'https://file-size-limiter-67005a553eac.herokuapp.com/check-file-size'
files = {'file': open('path/to/your/file.pdf', 'rb')}

response = requests.post(url, files=files)
print(response.json())
