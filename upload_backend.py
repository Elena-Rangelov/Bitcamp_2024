import requests

url = "https://production.talentide.talentide-app.workers.dev/"
files = {'file': open('your_pdf_file.pdf', 'rb')}

response = requests.post(url, files=files)

if response.status_code == 201:
  print("File uploaded successfully!")
else:
  print("Error uploading file:", response.text)
