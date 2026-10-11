# 02 — Understanding LLMs

Hey, welcome to lesson two.

We've all asked an AI a question and received an answer that sounded ridiculously confident. Sometimes it's right. Sometimes it confidently tells you something that makes you wonder whether it even read your question.

That confidence is exactly why this lesson exists.

Before we connect Python to a model provider and watch text appear on screen like magic, we're going to slow down and ask the important questions: what *is* a Large Language Model, how does it actually generate text, and why does it sometimes sound so sure about something that turns out to be completely wrong?

Understanding those answers now will make every coding lesson that follows ten times easier.

## Why are these lessons text-only?

You might have noticed something: this module contains no Python files. No `import` statements, no API calls, no `pip install`. Just explanations, diagrams, and questions.

That's intentional.

Learning Generative AI is not just about copying an API call, pasting in a key, and printing whatever comes back. If that's all we did, you'd be able to call a model and still have no idea what you're actually talking to, why it fails, or what to do when it does.

So these first lessons are conceptual. They're about building a correct mental model of:

- What the model is and isn't
- How it generates text
- What training and inference actually mean
- Why context limits matter
- Why models hallucinate, and why fluent language is not proof of correctness

Once that foundation is in place, the code will make a lot more sense. When we eventually write our first API call, you'll know what's happening on the other side of that request — and you'll be equipped to debug it, improve it, and build on it.

Good learning material takes time to develop. We'd rather explain things properly than rush into implementation and leave you guessing.

One more thing: the actual code, SDKs, and API calls come next. Lesson 03 (Tokens and Context Windows) is already on the roadmap, and after that we start writing real Python.

## What you'll learn

By the end of this module, you should be able to:

- Explain what an LLM is, in plain language, without buzzwords
- Describe how AI, machine learning, deep learning, and LLMs relate to each other
- Explain next-token prediction and why it matters
- Tell the difference between training, fine-tuning, and inference
- Explain what model parameters and context windows are
- Recognize why LLMs hallucinate and why confidence is not accuracy

## Lessons

| # | Lesson | What it covers |
|---|--------|----------------|
| 01 | [What Is an LLM?](01-what-is-an-llm.md) | The big picture: what "large," "language," and "model" actually mean, and where LLMs sit in the AI family tree. |
| 02 | [How LLMs Generate Text](02-how-llms-generate-text.md) | Tokenization, next-token prediction, and why answers are built one piece at a time. |
| 03 | [Training vs. Inference](03-training-vs-inference.md) | What happens when a model learns vs. when it answers you, and why chatting with a model doesn't teach it anything. |
| 04 | [Model Parameters and Context](04-model-parameters-and-context.md) | What parameters are, what a context window is, and why your long conversation eventually gets forgotten. |
| 05 | [Limitations and Hallucinations](05-limitations-and-hallucinations.md) | Why models sound confident when they're wrong, and what we can do about it. |

Each lesson includes a diagram you can open and edit in [Excalidraw](https://excalidraw.com/), common misconceptions, a recap, and a few practice questions.

## How to learn from this module

Read the lessons in order. They build on each other. After each one, try explaining the concept out loud, as if you were teaching a friend — if you can explain it simply, you actually understand it.

When you finish a lesson, attempt the practice questions in [practice-questions.md](practice-questions.md) before peeking at the answer key.

## Not a fan of learning from text? That's okay!

Let's be real. Everyone learns differently. Some people love reading explanations, while others would rather watch someone explain a concept on YouTube.

If a topic here doesn't click for you, feel free to look for YouTube videos that explain it visually. There's absolutely nothing wrong with that. Sometimes, hearing someone explain an idea or watching a diagram being drawn makes everything fall into place.

I might not be able to teach you through my own voice or video lessons here, but that's where this repository comes in.

**Use videos to understand the concepts, then come back here for the code, examples, and projects.**

You can use both resources together, learn at your own pace, and revisit anything that feels confusing. The goal isn't to learn everything from one source. It's to understand what you're learning and eventually build something with it.

And if you find a concept difficult, don't give up on it just yet. Try another explanation, draw it out, or work through an example.

We're here to learn, not to rush.

## Completion checklist

- [ ] I can explain what an LLM is without using the word "revolutionary"
- [ ] I can describe how AI, ML, deep learning, and LLMs relate
- [ ] I can explain next-token prediction with a simple example
- [ ] I can explain the difference between training and inference
- [ ] I can explain why context windows matter
- [ ] I can explain what a hallucination is and why it happens
- [ ] I've attempted the practice questions and checked my answers

## What's next

Up next is **Lesson 03 — Tokens and Context Windows**, where we dig into how models break text into tokens and why those tokens have a cost. That's where we'll start counting what we send to a model and why it matters.

After that: prompts, messages, and then — finally — your first real API call in Python.

## Resources

- [Resources and further reading](resources.md) — verified documentation and learning material for this module

---

**Maintained by Aryan | ISTMX**

Learning in public, one concept at a time.
