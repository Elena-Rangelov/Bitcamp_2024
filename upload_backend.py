from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.post("/upload")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    try:
        content = await pdf_file.read()
        # Replace with your actual KV storage logic
        # This part is pseudocode for demonstration purposes
        await store_in_talentide_kv(pdf_file.filename, content)
        return {"message": f"PDF '{pdf_file.filename}' uploaded successfully!"}
    except Exception as e:
        print(f"Error uploading PDF: {e}")
        return {"message": "An error occurred during upload. Please try again."}

# Replace this function with your KV storage logic using Cloudflare Workers API
async def store_in_talentide_kv(filename, content):
    # Get KV namespace from environment variable
    namespace = os.environ.get("TALENTIDE_KV_NAMESPACE")
    if not namespace:
        raise Exception("TALENTIDE_KV_NAMESPACE environment variable not set!")

    # Use Cloudflare Workers API to access KV
    url = f"https://api.cloudflare.com/v1/storage/kv/namespaces/{namespace}/values/{filename}"
    headers = {
        "Authorization": f"Bearer {your_cloudflare_api_token}"  # Replace with your API token
    }
    async with aiohttp.ClientSession() as session:
        async with session.put(url, headers=headers, data=content) as response:
            if response.status != 200:
                raise Exception(f"Error storing PDF: {await response.text()}")
