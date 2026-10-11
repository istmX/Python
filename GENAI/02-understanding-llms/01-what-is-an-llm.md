# 01 — What Is an LLM?

## Learning objectives

By the end of this lesson, you should be able to:

- Explain what a Large Language Model is in plain language
- Break down what "large," "language," and "model" each mean
- Place LLMs in the bigger picture of AI, machine learning, and deep learning
- Tell the difference between an AI application and the model behind it
- Describe the general flow from a user's question to a generated answer

## The name is the definition

"Large Language Model" is one of those terms that sounds intimidating until you realize it's just three ordinary words glued together. Let's take them one at a time.

**Language** — the model works with language. Text in, text out. It reads and writes human language: English, Hindi, Python error messages, your half-finished emails, all of it.

**Model** — in machine learning, a "model" is a mathematical system that learned patterns from data. Think of it like a very sophisticated summary of everything it has seen during training. It doesn't store the training data itself; it stores *patterns* about how language works.

**Large** — the model is enormous. We're talking about systems with billions of internal settings (called *parameters*, which we'll cover properly in lesson 04) that were trained on staggering amounts of text. The "large" is doing a lot of work in that sentence.

So, put it together: a **Large Language Model is a very large mathematical system, trained on vast amounts of text, that has learned the statistical patterns of human language well enough to read a prompt and produce a plausible continuation of it.**

That last part is the key. An LLM doesn't "know" things the way you know things. It predicts what text should come next, based on patterns it absorbed during training. Sometimes that prediction is exactly what you needed. Sometimes it's confidently, fluently wrong. More on that in lesson 05.

## Where does an LLM sit in the AI family tree?

People throw around "AI," "machine learning," and "deep learning" like they're the same thing. They're related, but they're not identical. Here's the nesting:

| Term | What it means | Analogy |
|---|---|---|
| **Artificial Intelligence (AI)** | The broad field of making machines do things that seem intelligent | The whole "smart machines" industry |
| **Machine Learning (ML)** | A subset of AI where machines learn patterns from data instead of following hand-written rules | Teaching by showing examples rather than writing a rulebook |
| **Deep Learning** | A subset of ML that uses neural networks with many layers ("deep" = many layers) | A particular, very powerful way of learning from examples |
| **LLM** | A large language model — a deep learning model trained on text to predict language | One very famous resident of the deep learning house |

So: every LLM is a deep learning model, every deep learning model is machine learning, and all machine learning is AI. But not all AI is an LLM. A chess engine is AI. A spam filter is machine learning. An LLM is something more specific.

## What are LLMs actually used for?

You've probably already used more LLMs than you realize:

- **Chatbots** — ChatGPT, Gemini, Claude. The obvious ones.
- **Coding assistants** — tools that explain errors, suggest fixes, or write boilerplate. If you've ever pasted a traceback into a chat and gotten a useful answer, that was an LLM.
- **Summarization** — turning a 40-page report into five bullet points.
- **Translation** — converting text between languages.
- **Writing assistance** — drafting emails, rephrasing paragraphs, brainstorming names for your variables at 1 AM.
- **Search and question answering** — "what does this error mean?" is a language question, and LLMs are good at language questions.

The common thread: all of these are tasks where the input is language and the output is language. That's the LLM's home turf.

## The application vs. the model — an important distinction

Here's a tripwire that catches a lot of beginners: **the thing you talk to is not the model.**

When you open a chat app and type a message, you're talking to an **AI application**. The application is the software built around the model — the interface, the conversation history, the safety filters, the retrieval system, the code that formats your prompt and displays the response.

The **model** is the engine under the hood. It receives text and returns text. It has no idea what a "chat" is. It doesn't know your name. It doesn't remember your previous message unless the application explicitly sends it again.

This distinction matters enormously when things go wrong. If a chat app gives a weird answer, the cause might be the model — or it might be how the application packaged your prompt, what context it included, or a safety filter that intercepted the response. When we start building our own applications in later lessons, *we* become the people responsible for that packaging layer.

## From question to answer: the general flow

Let's trace what happens when you ask an AI application a question. The exact details vary between applications, but the general shape looks like this:

![High-level overview of how a user, an AI application, and an LLM connect](diagrams/01-llm-overview.excalidraw)

**How to read this diagram:**

1. **You type a question** — "Why is my Python code throwing a TypeError?"
2. **The AI application prepares the request** — it takes your question, combines it with conversation history and any system instructions, and packages everything into a format the model understands. Real applications may add extra steps here: safety checks, retrieval of relevant documents, tool calls, post-processing.
3. **The LLM processes the text** — it reads the full input and predicts what should come next, one piece at a time (lesson 02 explains exactly how).
4. **The model returns a generated response** — text, produced token by token.
5. **The application delivers it to you** — possibly after formatting, filtering, or checking it.

Notice what's *not* in that diagram: a database of answers. The model is not looking up your question in a FAQ. It's generating a response from learned patterns, every single time. That's why the same question can get slightly different answers, and why the model can produce something fluent that happens to be wrong.

Also notice the dashed box around the application: real applications vary wildly in what they add. A bare-bones app might send your text straight to the model. A sophisticated one might retrieve documentation, run searches, execute code, and check safety — all before you see a single word. Don't assume every AI product works identically under the hood.

## Common misconceptions

**❌ "The model understands me like a person does."**
It predicts text. Impressively well, sometimes eerily well — but prediction is not understanding. There's no little person in there nodding along.

**❌ "The model searched the internet for your answer."**
A standard LLM API call does not browse the web. It generates from patterns learned during training. (Some applications *add* web search around the model — that's the application's feature, not the model's.)

**❌ "The model remembers our conversation."**
The model itself remembers nothing between requests. If a chat app seems to remember, it's because the application keeps the history and resends it with every message. We'll prove this to ourselves in lesson 04.

**❌ "More parameters always means a better model."**
Parameter count is one factor among many: training data quality, architecture, fine-tuning, and evaluation all matter. A smaller, well-trained model can beat a larger, sloppy one for specific tasks.

## Recap

- An LLM is a very large mathematical system trained on text to predict language.
- LLMs live inside the deep learning ⊂ machine learning ⊂ AI family tree.
- The AI application is the software around the model; the model is just the text-in, text-out engine.
- A response is generated from learned patterns, not retrieved from a database of answers.
- Real applications add their own steps — safety, retrieval, tools — and no two are built exactly the same.

## Practice questions

Attempt these before checking the [answer key](practice-questions.md#answer-key). Full questions are listed in [practice-questions.md](practice-questions.md).

1. In your own words, what does each word in "Large Language Model" mean?
2. Is every machine learning system an LLM? Is every LLM a machine learning system? Explain.
3. Your friend says "the chatbot looked up the answer on the internet." Why is that probably not what happened?
4. Using the diagram, describe the journey of your question from keyboard to answer.

## References

- [Google Gemini API documentation](https://ai.google.dev/gemini-api/docs) — official overview of how hosted models are used
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) — free course covering LLMs conceptually and practically
- [OpenAI Platform documentation](https://platform.openai.com/docs) — official docs on models and the API
