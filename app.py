from flask import Flask, request, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def get_file_size(file):
    file.seek(0, os.SEEK_END)  # Go to the end of the file
    size = file.tell()         # Get the size of the file
    file.seek(0, os.SEEK_SET)  # Reset the file pointer to the beginning
    return size

@app.route('/check-file-size', methods=['POST'])
def check_file_size():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not (file.filename.endswith('.pdf') or file.filename.endswith('.docx')):
        return jsonify({'error': 'Unsupported file type'}), 400

    file_size = get_file_size(file)

    if file_size > MAX_FILE_SIZE:
        return jsonify({'error': 'File size exceeds 5MB limit'}), 400

    return jsonify({'message': 'File successfully uploaded', 'size': file_size})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
