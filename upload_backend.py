from flask import Flask, request, jsonify
from flask_cors import CORS
from cloudflare import Cloudflare

app = Flask(__name__)
CORS(app)

# Initialize Cloudflare client
cf = Cloudflare("talentide.app@gmail.com", "c2659d7873c9a94e4087d94de9206cf537074", "9b40615208e01c94610c2354916096c2")

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


# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from cloudflare import Cloudflare

# app = Flask(__name__)
# CORS(app)

# # Initialize Cloudflare client
# cf = Cloudflare("talentide.app@gmail.com", "7d9fTTtYIqIe3ChieVZMx9K9wSxIy3E_qkSpbHO7", "9b40615208e01c94610c2354916096c2")

# @app.route('/store-pdf', methods=['POST'])
# def store_pdf():
#     pdf_file = request.files['pdf_file']
#     if pdf_file.filename == '':
#         return jsonify({'error': 'No file uploaded'}), 400

#     try:
#         # Save the PDF file to Cloudflare Workers KV
#         key = 'uploads/' + pdf_file.filename
#         with pdf_file as file_data:
#             cf.upload_file(key, file_data.read())
        
#         return jsonify({'message': 'File uploaded successfully'}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from cloudflare import Cloudflare

# app = Flask(__name__)
# CORS(app, resources={r"/store-pdf": {"origins": "https://talentide.us"}})

# # Initialize Cloudflare client
# # Replace placeholders with your actual Cloudflare credentials
# cf = Cloudflare("talentide.app@gmail.com", "c2659d7873c9a94e4087d94de9206cf537074", "9b40615208e01c94610c2354916096c2")

# @app.route('/store-pdf', methods=['POST'])
# def store_pdf():
#     pdf_file = request.files['pdf_file']
#     if pdf_file.filename == '':
#         return jsonify({'error': 'No file uploaded'}), 400

#     try:
#         # Save the PDF file to Cloudflare Workers KV
#         key = 'uploads/' + pdf_file.filename
#         with pdf_file as file_data:
#             cf.upload_file(key, file_data.read())
        
#         return jsonify({'message': 'File uploaded successfully'}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)







# from flask import Flask, request, send_from_directory
# import os

# app = Flask(__name__)

# # Define the folder where uploaded files will be saved
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def home():
#     return send_from_directory('templates', 'index.html')

# @app.route('talentide.us/templates/upload.html', methods=['POST'])
# def upload_file():
#     if 'pdf_file' not in request.files:
#         return "No file uploaded", 400

#     file = request.files['pdf_file']
#     if file.filename == '':
#         return "No selected file", 400

#     # Save the uploaded file to the specified folder
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

#     return "File uploaded successfully"

# if __name__ == '__main__':
#     app.run(host='https://talentide.us/templates/upload.html', port=443 , debug=True)
