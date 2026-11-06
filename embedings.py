from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

text = "Eiffel Tower is in Paris and is a famous landmark, it is 324 meters tall"

res = client.embeddings.create(
    input=text,
    model='text-embedding-3-small'
)

print("Vector Embeddings", res.data[0].embedding)
