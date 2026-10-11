
"""
Let's build a mini LLM assistant using Google's Gemini API.

First, install the required packages:

    pip install google-genai python-dotenv

Or, if you're using uv:

    uv add google-genai python-dotenv

Create a .env file and add your API key:

    GEMINI_API_KEY=your_api_key_here

Also, add .env to your .gitignore so your API key doesn't
accidentally end up on GitHub.

We're using Google's official google-genai SDK to communicate
with Gemini.

The chat session will maintain conversation history while
the program is running.

Streaming lets us see the response as it is generated,
instead of waiting for the entire answer.
"""





#import the required libraries
 
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv() #load environment variables from .env file

API_KEY = os.getenv("GEMINI_API_KEY") 


def main():
    client = genai.Client(api_key=API_KEY)

    memory = []

    while True:
        userInput = input("Enter your prompt: ")

        if userInput.lower() == "exit":
            break

        memory.append({
            "role": "user",
            "parts": [{"text": userInput}]
        })

        responseText = ""

        for chunk in client.models.generate_content_stream(
            model="gemini-3.8-flash",
            contents=memory,
            config=types.GenerateContentConfig(
                temperature=0.7,
                system_instruction=(
                    "You are a helpful assistant. "
                    "Answer naturally and clearly."
                ),
            ),
        ):
            if chunk.text:
                print(chunk.text, end="", flush=True)
                responseText += chunk.text

        print("\n")

        memory.append({
            "role": "model",
            "parts": [{"text": responseText}]
        })


if __name__ == "__main__":
    main()

