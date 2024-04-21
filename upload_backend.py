from flask import Flask, request
import requests
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/path/to/your/upload/folder'
WORKERS_ROUTE = 'https://your-workers-route.your-account.workers.dev'

@app.route('/')
def index():
    return open('upload.html', 'r').read()

@app.route('/upload.html', methods=['POST'])
def upload_file():
    pdf_file = request.files['pdfFile']
    if pdf_file.filename != '':
        pdf_file.save(os.path.join(UPLOAD_FOLDER, pdf_file.filename))
        upload_to_workers(pdf_file.filename)
        return 'File uploaded successfully and stored in Cloudflare KV.'
    else:
        return 'No file selected.'

def upload_to_workers(filename):
    url = f'{WORKERS_ROUTE}/storepdf'
    files = {'pdfFile': open(os.path.join(UPLOAD_FOLDER, filename), 'rb')}
    response = requests.post(url, files=files)
    print(response.text)

if __name__ == '__main__':
    app.run(debug=True)
