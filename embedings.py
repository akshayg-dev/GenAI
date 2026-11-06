from dotenv import load_dotenv
from openai import OpenAI
from google import genai
import os

load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")

# client = OpenAI(api_key=api_key)
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

text = "Eiffel Tower is in Paris and is a famous landmark, it is 324 meters tall"

# res = client.embeddings.create(
#     input=text,
#     model='text-embedding-3-small'
# )

res = client.models.embed_content(
    model="gemini-embedding-001",
    contents=text
)

print("Vector Embeddings: ", res.embeddings[0].values)
