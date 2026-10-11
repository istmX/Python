# Gemini Mini LLM Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Gemini" />
  <img src="https://img.shields.io/badge/Memory-Conversation%20History-8B5CF6?style=for-the-badge" alt="Conversation memory" />
  <img src="https://img.shields.io/badge/Streaming-Enabled-16A34A?style=for-the-badge" alt="Streaming enabled" />
</p>

<p align="center">
  <b>A small Python project to understand LLMs, APIs, streaming, and conversation memory.</b>
  <br />
  Built while learning Generative AI, one prompt at a time.
</p>

---

## Hey there!

Welcome to my little Gemini-powered AI assistant!

This project is a simple command-line chatbot built with Python and Google's Gemini API. It accepts your prompts, streams the model's responses as they arrive, and maintains conversation history so that you can ask follow-up questions.

No complicated frameworks. No massive architecture. Just Python, an API, and a little curiosity.

## What does it do?

- **Chat with Gemini:** Send questions and receive AI-generated responses.
- **Stream responses:** See text appear progressively instead of waiting for the complete answer.
- **Maintain conversation context:** Send previous messages back to the model so it can follow the conversation.
- **Use environment variables:** Keep your API key outside your Python source code.
- **Stay beginner-friendly:** Learn the fundamentals before jumping into large AI frameworks.

## How it works

```mermaid
flowchart TD
    A(["You enter a prompt"]) --> B["Python receives input"]
    B --> C["Save prompt in memory"]
    C --> D["Send conversation history to Gemini"]
    D --> E["Gemini generates a response"]
    E --> F["Stream text chunks to terminal"]
    F --> G["Collect the complete response"]
    G --> H["Save assistant response in memory"]
    H --> I{"Continue chatting?"}
    I -- Yes --> A
    I -- "Type exit" --> J(["End conversation"])

    classDef user fill:#DBEAFE,stroke:#2563EB,color:#1E3A8A,stroke-width:2px
    classDef python fill:#D1FAE5,stroke:#059669,color:#064E3B,stroke-width:2px
    classDef ai fill:#EDE9FE,stroke:#7C3AED,color:#4C1D95,stroke-width:2px
    classDef stream fill:#FEF3C7,stroke:#D97706,color:#78350F,stroke-width:2px
    classDef end fill:#FCE7F3,stroke:#DB2777,color:#831843,stroke-width:2px

    class A user
    class B,C,G,H python
    class D,E ai
    class F stream
    class I,J end
```

The basic idea is simple: your Python program sends the conversation to Gemini, receives the answer as a stream of chunks, and stores the completed answer for the next turn.

## Tech stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Google Gemini API | Generates AI responses |
| `google-genai` | Google's official Python SDK |
| `python-dotenv` | Loads the API key from `.env` |
| Python list | Stores conversation history during execution |

## Project structure

```text
gemini-mini-assistant/
├── main.py
├── .env
├── .gitignore
└── README.md
```

- `main.py` — The chatbot implementation.
- `.env` — Your private Gemini API key.
- `.gitignore` — Prevents sensitive files from being committed.
- `README.md` — Project documentation.

## Getting started

### 1. Clone or download the project

If the project is hosted on GitHub, clone your repository:

```bash
git clone YOUR_REPOSITORY_URL
cd gemini-mini-assistant
```

Alternatively, create a folder and place your Python file inside it.

### 2. Install the dependencies

Using `pip`:

```bash
pip install google-genai python-dotenv
```

Using `uv`:

```bash
uv add google-genai python-dotenv
```

These are the only external packages this project needs.

### 3. Get a Gemini API key

Visit [Google AI Studio](https://aistudio.google.com/apikey) and create an API key if API access is available to your account.

Create a `.env` file in your project directory:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

Replace the placeholder with your real key.

**Keep your API key private.** Never paste it into your source code, screenshots, public issues, or GitHub commits.

### 4. Configure `.gitignore`

Add the following lines to your `.gitignore` file:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
```

This helps keep your API key and local Python environment out of version control.

### 5. Run the assistant

```bash
python main.py
```

Start chatting! Type `exit` to end the session.

## Understanding the code

### 1. Importing libraries

```python
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
```

- `os` lets Python access environment variables.
- `load_dotenv` loads variables from your `.env` file.
- `genai` provides the Google Gemini SDK.
- `types` provides configuration classes for model requests.

### 2. Loading the API key

```python
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
```

The API key is loaded from your environment instead of being hardcoded into the program.

This is a safer way to manage credentials, although you should also avoid logging the key or exposing it through error messages.

### 3. Creating the client

```python
client = genai.Client(api_key=API_KEY)
```

The client is the connection point between your Python application and the Gemini API. Your program uses it to send requests to the model.

### 4. Creating conversation memory

```python
memory = []
```

This empty list stores the messages exchanged during the current session.

When the user sends a message, it is added to the list:

```python
memory.append({
    "role": "user",
    "parts": [{"text": userInput}]
})
```

The `"user"` role identifies the message as coming from you.

After the assistant finishes responding, its answer is stored too:

```python
memory.append({
    "role": "model",
    "parts": [{"text": responseText}]
})
```

Now the model can receive both sides of the conversation on the next request.

**Important:** This is conversation history, not permanent memory. The list exists only while your program is running.

### 5. Sending the conversation to Gemini

```python
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
```

Here's what the main arguments do:

- `model` selects the Gemini model to use. Make sure the model identifier is available to your account.
- `contents=memory` sends the conversation history, allowing the model to use previous turns as context.
- `temperature=0.7` configures response randomness. It is a generation setting, not a guarantee of creativity or accuracy.
- `system_instruction` describes the assistant's intended behavior.
- `generate_content_stream()` returns response chunks progressively.

The history is sent again with each request. That is what allows the model to refer to earlier messages without a separate database.

### 6. Streaming the response

```python
responseText = ""

for chunk in client.models.generate_content_stream(...):
    if chunk.text:
        print(chunk.text, end="", flush=True)
        responseText += chunk.text
```

This is the part that makes the assistant feel interactive.

- `chunk.text` contains text available in the current response chunk.
- `end=""` prevents Python from inserting a newline after every chunk.
- `flush=True` asks Python to display the text immediately.
- `responseText += chunk.text` collects the chunks into one complete response.

The same response can therefore be displayed live and saved for future context.

### 7. Keeping the conversation going

```python
memory.append({
    "role": "model",
    "parts": [{"text": responseText}]
})
```

Once streaming finishes, the complete assistant response is appended to the history. The loop then asks for another prompt.

When you enter `exit`, the loop ends.

## Example conversation

The following is an illustrative conversation showing how the assistant can respond. Actual responses may vary.

```text
Enter your prompt: Hey, introduce yourself

Hey Aryann! Nice to meet you. How's it going?
What can I help you with today?

Enter your prompt: what is gen ai

Gen AI (short for Generative Artificial Intelligence)
refers to a type of AI that can create new content
rather than just analyzing or classifying existing data.

Traditional AI often predicts or classifies things.
Generative AI can create text, images, code, audio,
and other content based on what it has learned.

For example, it can write an email, explain a concept,
generate code, or create an image from a description.

Enter your prompt: what is my name

Your name is Aryann!

Enter your prompt: exit
```

The example's name response is not guaranteed. The model may infer a name from previous messages, but it can also make an incorrect guess. The assistant can only use the context supplied to it and what the model has learned; it does not automatically know your personal identity.

## What is conversation memory, really?

Imagine this conversation:

1. You: `My favorite language is Python.`
2. Assistant: `Nice! Python is great for AI development.`
3. You: `What is my favorite language?`

If the previous messages are included in `memory`, the model can answer using the earlier conversation.

Without that history, the model may not know what you told it.

There are three useful concepts to distinguish:

| Concept | What it means in this project |
|---|---|
| Conversation history | The messages stored in the `memory` list |
| Context | The information sent to the model for a particular request |
| Persistent memory | Information saved somewhere durable and loaded in a later run |

This project implements the first two. It does **not** yet implement persistent memory.

## Current limitations

This is a learning project, not a production-ready assistant.

- **Temporary memory:** Restarting the program clears the list.
- **Growing context:** Every turn sends the previous messages again, increasing token usage as the conversation grows.
- **No database:** Conversations are not saved to a file or database.
- **No guaranteed accuracy:** LLMs can make mistakes or hallucinate.
- **API limits:** Requests may fail because of quota, rate limits, network problems, permissions, or model availability.
- **Basic error handling:** The current script does not explicitly handle every possible API error.

These are natural limitations for a first project. You can improve them as you learn more.

## Troubleshooting

**`ModuleNotFoundError`**

Install the dependencies in the Python environment you're using:

```bash
pip install google-genai python-dotenv
```

**API key is missing or authentication fails**

Check that `.env` is in the correct directory, the variable is spelled `GEMINI_API_KEY`, and the key is valid.

**Model not found**

Check the available model names in the [Gemini models documentation](https://ai.google.dev/gemini-api/docs/models).

**Quota or rate-limit error**

Check your account's API usage and limits. Availability and free-tier limits can vary.

**The assistant forgets everything after restarting**

That is expected. `memory` is a Python list in RAM. Saving conversations to JSON or a database would be a future improvement.

## What I learned from this project

- How to connect a Python application to an LLM API.
- How to manage API keys with environment variables.
- How to send prompts and configure model behavior.
- How streaming responses work.
- How to maintain conversation context using a list.
- Why conversation history is different from persistent memory.

## Official learning resources

- [Google Gen AI Python SDK](https://googleapis.github.io/python-genai/) — SDK documentation and Python examples.
- [Gemini API documentation](https://ai.google.dev/gemini-api/docs) — Learn how to use the API.
- [Gemini models](https://ai.google.dev/gemini-api/docs/models) — Check supported models and their capabilities.
- [Google AI Studio](https://aistudio.google.com/) — Explore models and manage API keys.
- [Python documentation](https://docs.python.org/3/) — The official Python reference.
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Documentation for loading `.env` files.

## What's next?

Possible improvements for future versions:

- Save and restore conversations using JSON.
- Add a command to clear conversation history.
- Handle API errors and rate limits more gracefully.
- Add a maximum history length to control token usage.
- Experiment with different system instructions and model settings.
- Explore tools, structured outputs, and eventually retrieval-augmented generation (RAG).

One step at a time. Understand the fundamentals first; the fancy agent frameworks can wait.

---
