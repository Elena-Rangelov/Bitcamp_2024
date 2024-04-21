# import requests

# def upload_pdf_to_worker(pdf_file_path):
#     url = 'https://your-worker-subdomain.your-account.workers.dev/upload'
#     files = {'pdfFile': open(pdf_file_path, 'rb')}

#     try:
#         response = requests.post(url, files=files)
#         if response.ok:
#             return response.text  # You can handle the response as needed
#         else:
#             return 'Error uploading PDF file.'
#     except requests.RequestException as e:
#         return f'Error: {e}'

# # Example usage:
# pdf_file_path = '/path/to/your/pdf/file.pdf'
# result = upload_pdf_to_worker(pdf_file_path)
# print(result)
