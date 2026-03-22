import os
from huggingface_hub import AsyncInferenceClient
from dotenv import load_dotenv

load_dotenv()

async def generate_response(prompt: str) -> str:
    token = os.getenv("HUGGINGFACE_TOKEN")
    if not token:
        return "Error: HUGGINGFACE_TOKEN is not set in your .env file."
    
    # Initialize the official client
    client = AsyncInferenceClient(token=token)
    
    # Format messages to clearly send a chat message
    messages = [{"role": "user", "content": prompt}]
    
    try:
        # We can finally use the original Llama 3 model you requested, as your token allows it!
        response = await client.chat_completion(
            messages=messages,
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error communicating with HuggingFace API: {e}"
