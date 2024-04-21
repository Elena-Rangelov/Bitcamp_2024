from flask import Flask, request, jsonify
from flask_cors import CORS
from cloudflare import Cloudflare

app = Flask(__name__)
CORS(app, resources={r"/store-pdf": {"origins": "https://talentide.us"}})

# Initialize Cloudflare client
cf = Cloudflare("talentide.app@gmail.com", "q86E-uByo12Vu3GmqHS3yTJ-YFWYQlqryB8_4-9i", "9b40615208e01c94610c2354916096c2")

@app.route('/store-pdf', methods=['POST'])
def store_pdf():
    pdf_file = request.files['pdf_file']
    if pdf_file.filename == '':
        return jsonify({'error': 'No file uploaded'}), 400

    try:
        # Save the PDF file to Cloudflare Workers KV
        key = 'uploads/' + pdf_file.filename
        with pdf_file as file_data:
            cf.upload_file(key, file_data.read())
        
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
