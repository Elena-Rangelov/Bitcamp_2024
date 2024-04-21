from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    pdf_file = request.files['pdfFile']
    if pdf_file:
        response = requests.post('https://your-worker-subdomain.your-account.workers.dev/storepdf', files={'pdfFile': pdf_file})
        return response.text
    else:
        return 'No file selected.'

if __name__ == '__main__':
    app.run(debug=True)
