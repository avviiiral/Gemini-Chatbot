from google import genai
from dotenv import load_dotenv
import os

load_dotenv()  # 🔑 THIS WAS MISSING

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

models = client.models.list()

for m in models:
    print(m.name)
