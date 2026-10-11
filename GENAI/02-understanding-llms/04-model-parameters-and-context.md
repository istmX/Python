# 04 — Model Parameters and Context

## Learning objectives

By the end of this lesson, you should be able to:

- Explain what model parameters are at a high level
- Explain why parameter counts are discussed when comparing models
- Explain why a larger parameter count doesn't automatically mean better performance
- Explain what a context window is
- Explain how conversation messages consume context
- Explain the difference between context length and persistent memory
- Explain why long conversations get truncated or summarized
- Understand that limits differ between providers and models

## Parameters: the model's frozen knowledge

In lesson 03 we met **parameters** — the model's internal numerical settings, tuned during training and frozen at the end of it. Let's go one level deeper, because parameter counts are one of the most common ways people compare models.

When you see a model described as "8 billion parameters" or "405 billion parameters," that number is the count of internal numerical values the model uses to process text. During training, each of those values gets adjusted, tiny step by tiny step, until the model's predictions improve. After training, they're fixed.

Why do people care about the count?

- **Capacity:** more parameters generally means more room to encode patterns — more facts, more styles, more nuance.
- **Cost:** more parameters generally means more compute to train and to run, which means higher prices and slower responses.
- **Rough benchmarking:** it's a quick, if crude, way to compare model sizes.

But here's the part that trips people up: **parameter count is not a performance guarantee.**

Think of it like engine displacement in cars. A bigger engine *can* mean more power, but it doesn't tell you about the transmission, the tires, the tuning, or the driver. Two cars with the same engine can perform very differently. Similarly:

- **Training data quality** matters as much as size. A model trained on carefully curated data can beat a bigger model trained on junk.
- **Architecture and training technique** matter. Better methods extract more from fewer parameters.
- **Fine-tuning and alignment** matter. A model can be adapted to be excellent at a specific task without being the biggest.
- **Evaluation is the only real answer.** The way to know if a model is good at something is to test it at that something — not to read its parameter count.

So when you compare models, treat parameter count as one input among many — never as the score.

## Context: the model's working memory

If parameters are the model's long-term knowledge, **context** is its short-term working memory: everything the model can "see" right now, in this one request.

Every input you send has a size limit called the **context window** — the maximum number of tokens the model will accept in a single request. That window has to fit everything:

![The context window holding system instructions, conversation history, the current message, and room for the response](diagrams/04-context-window.excalidraw)

**How to read this diagram:**

- The large outer rectangle is the **context window** — the total space available for one request.
- Inside it: **system instructions** (the app's standing directions for the model), the **conversation history** (your previous messages and the model's previous replies), and the **current message** (what you just typed).
- The empty space is the **room for the generated response** — the model's output also takes up context.
- The exact arrangement and accounting vary between models and APIs. Don't assume every provider packs the window identically.

Here's the part that surprises people: **conversation history consumes context.** Every message you send, and every reply the model gives, eats into the same finite window. A chat that started small eventually fills it up.

## Context window ≠ memory

This is one of the most important distinctions in this lesson:

- **Context window** is temporary. It exists for one request. The model has no storage between requests — ask it something tomorrow, and it starts from whatever the application sends it.
- **Persistent memory** is something the *application* builds around the model. If a chat app remembers your preferences, it's because the app stores them (in a database, a file, whatever) and includes them in each request — not because the model remembers.

When a long conversation exceeds the context window, the application has to do something about it. Common strategies:

- **Truncation** — drop the oldest messages and keep the recent ones.
- **Summarization** — compress earlier conversation into a shorter summary and include that instead.
- **Sliding windows** — keep only the most recent N messages.
- **Selective retention** — keep important messages and discard the rest.

That's why a very long chat can "forget" something you said hours ago. The model isn't being difficult — that content simply isn't in the request anymore.

## Limits differ between providers and models

There is no universal context window size. A model's limit depends on the provider and the specific model:

- One model might handle 128 thousand tokens per request; another might handle 2 million.
- The limit includes *everything*: your prompt, the system instructions, the conversation history, retrieved documents, and the generated output.
- Providers also impose separate rate and quota limits (requests per minute, tokens per day) — those are account limits, not model limits, but they affect your app just the same.

Always check the current documentation for the specific model you're using. Don't carry a limit from one model to another, and don't assume a limit you read about last year is still accurate — these change.

## Why this matters for your code

When we start writing API calls in later lessons, context becomes a practical concern, not just a concept:

- Every token you send costs money (on most providers) and takes time.
- A prompt stuffed with irrelevant history wastes context and can dilute the answer.
- If your application handles long conversations, *you* are responsible for managing what goes into each request.

The model won't warn you when you're running out of context. Your application has to manage it.

## Common misconceptions

**❌ "The context window is the model's memory."**
It's a per-request input limit. The model has no memory between requests unless the application gives it one.

**❌ "All models have the same context limit."**
Limits vary by provider and model. Always check the docs for the model you're using.

**❌ "The context limit is very large, so I don't need to think about it."**
For simple demos, maybe. For real applications with long conversations, context management is a genuine engineering problem.

**❌ "If the model 'remembers' something from earlier, it stored it."**
Either the application resent the history, or the application has its own memory system. The model itself stored nothing.

## Recap

- **Parameters** are the model's frozen internal settings — capacity, not capability. Bigger isn't automatically better.
- **Context** is everything the model can see in one request: system instructions, history, your message, and the response.
- The **context window** is the token limit for that request. History consumes it.
- **Context ≠ memory.** Persistent memory is built by the application around the model.
- Long conversations get truncated, summarized, or windowed by the application.
- Limits differ between providers and models — always check current docs.

## Practice questions

Full questions are listed in [practice-questions.md](practice-questions.md).

1. What does a model's parameter count tell you — and what doesn't it tell you?
2. Why isn't a bigger model always a better model?
3. What has to fit inside a context window?
4. A chatbot forgets something you told it three days ago. Using this lesson, explain two possible reasons.
5. What's the difference between context length and persistent memory?

## References

- [Google Gemini token documentation](https://ai.google.dev/gemini-api/docs/tokens) — how tokens and context are counted by one major provider
- [Google Gemini API documentation](https://ai.google.dev/gemini-api/docs) — current model limits and capabilities
- [OpenAI Platform documentation](https://platform.openai.com/docs) — model reference including context limits
