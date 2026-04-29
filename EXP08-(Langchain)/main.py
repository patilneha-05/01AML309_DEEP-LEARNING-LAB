from dotenv import load_dotenv
import os
from google import genai

# Load .env
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=api_key)

# Generate content
response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="What is Artificial Intelligence? and how does it work?"
)

# Print response
print(response.text)