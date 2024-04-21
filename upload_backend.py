from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Define the folder where uploaded files will be saved
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return send_from_directory('templates', 'index.html')

@app.route('talentide.us/templates/upload.html', methods=['POST'])
def upload_file():
    if 'pdf_file' not in request.files:
        return "No file uploaded", 400

    file = request.files['pdf_file']
    if file.filename == '':
        return "No selected file", 400

    # Save the uploaded file to the specified folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    return "File uploaded successfully"

if __name__ == '__main__':
    app.run(host='https://talentide.us/templates/upload.html', port=443 , debug=True)
