# 03 — Training vs. Inference

## Learning objectives

By the end of this lesson, you should be able to:

- Explain the difference between training and inference
- Describe what model parameters are, conceptually
- Explain the broad purpose of loss functions and optimization
- Explain why calling a hosted LLM API performs inference, not training
- Distinguish between using a pretrained model, fine-tuning, and training from scratch
- Explain why chatting with a model does not teach it anything

## Two different jobs

People say "the model learned from data" and "the model answered my question" as if those are the same activity. They're not. They're two completely different phases of a model's life, with different inputs, different goals, and different costs.

- **Training** is when the model *learns*. It reads enormous amounts of text and adjusts its internal settings to get better at predicting language.
- **Inference** is when the model *works*. It takes your prompt and generates a response using what it already learned. Nothing inside the model changes.

A useful analogy: training is years of medical school. inference is seeing patients. A doctor doesn't go back to medical school between appointments — and a model doesn't retrain itself when you ask it a question.

## Training: where the learning happens

Training is the expensive, one-time (mostly) phase. Here's the broad shape of it:

1. **Gather training data** — massive amounts of text: books, articles, websites, code, conversations. The quality and mix of this data shape everything the model will be good at.
2. **Make predictions and measure mistakes** — the model predicts next tokens, and a **loss function** measures how wrong those predictions were. You can think of the loss as a score for "how surprised was the model by the correct answer." High loss = very surprised = bad prediction.
3. **Optimize** — an optimization process (a form of gradient descent) nudges the model's internal settings in the direction that reduces the loss. Then the model predicts again, measures again, nudges again. Billions of times.
4. **Repeat at scale** — this loop runs over the entire dataset, many times, on clusters of specialized hardware. Training a large model costs millions of dollars and months of compute.

The result of all that work is a **trained model**: a fixed set of internal settings that encode everything the model learned.

## What are parameters, anyway?

You've seen "7 billion parameters" or "70 billion parameters" in model announcements. What does that mean?

**Parameters are the model's internal numerical settings — the knobs that get tuned during training.**

A helpful way to picture it: imagine a sound mixer with billions of knobs. During training, each knob is turned by tiny amounts, over and over, until the output sounds right. After training, the knob positions are frozen. Those positions *are* the model's knowledge — not a database of facts, but a configuration that produces fluent, pattern-matching text.

A few things worth knowing:

- **More parameters generally means more capacity** — more room to encode patterns. But capacity is not the same as quality.
- **Parameter count alone doesn't determine performance.** Training data quality, architecture design, fine-tuning, and evaluation matter enormously. A smaller, well-trained model can outperform a larger, carelessly trained one on specific tasks.
- **Parameters are not memories.** A 70-billion-parameter model is not a 70-billion-fact encyclopedia. The relationship between parameters and "knowledge" is far more subtle than that.

## Inference: where you come in

Inference is everything that happens after training:

1. You send a prompt to a model (usually through an API).
2. The model runs its fixed parameters over your input.
3. It generates a response, token by token (lesson 02).
4. The response comes back to you.

**Crucially: the parameters do not change during inference.** The model is in "read-only" mode. Every user, every prompt, every conversation — the model itself stays exactly as it was when training ended.

This is why:

- **Chatting with a model doesn't teach it.** Your conversation is processed and discarded (from the model's perspective). The next user gets the same model you got.
- **Hosted API calls are inference.** When you call Gemini, OpenAI, or any hosted model, you're using a trained model as-is. You are not training anything.
- **Models have a knowledge cutoff.** Since the parameters are frozen, the model doesn't know about events after its training data ended — unless the application adds tools like web search.

## Training vs. inference, side by side

![Side-by-side comparison of the training process and the inference process](diagrams/03-training-vs-inference.excalidraw)

**How to read this diagram:**

- **Left — Training:** massive training data flows in, the model makes predictions, a loss function scores the mistakes, and an optimizer updates the parameters. The output is a trained model. The loop is the point: parameters are *updated*, again and again.
- **Right — Inference:** a user prompt flows into the already-trained model, the model generates a response, and the response goes back to the user. No update loop exists here — the parameters are *used*, never changed.

Same model, two completely different modes of operation.

## Pretrained, fine-tuned, and trained from scratch

You'll meet these three terms constantly. Here's the difference:

| Approach | What happens | When it's used |
|---|---|---|
| **Training from scratch** | Train a new model on a large dataset from zero | Building a foundation model; enormous cost; done by big labs |
| **Using a pretrained model** | Take an existing trained model and use it as-is | The most common case — including every API call we'll make |
| **Fine-tuning** | Take a pretrained model and continue training it on a smaller, specific dataset | Adapting a model to a domain, style, or task; updates parameters in a controlled way |

The key distinction: **training and fine-tuning update parameters; ordinary inference does not.** Fine-tuning is still training — just smaller, targeted, and starting from an existing model instead of zero.

When we call a hosted API in later lessons, we'll be using pretrained models. We won't be training or fine-tuning anything — and that's completely normal. Most developers never train a model; they use and adapt existing ones.

## Common misconceptions

**❌ "The model learns from our conversations."**
No. Your chats are inference requests. The model's parameters are frozen. (The *application* may store your history to resend it — that's the app remembering, not the model.)

**❌ "Bigger model = smarter, always."**
Parameter count is capacity, not capability. Data quality, training technique, and evaluation decide what a model can actually do.

**❌ "Training and inference are the same thing, just different words."**
They're opposite phases: one changes the model, the other uses it unchanged.

**❌ "Fine-tuning is just chatting with the model a lot."**
Fine-tuning is a deliberate training process on a prepared dataset. Casual conversation does nothing to the model.

## Recap

- **Training** = learning. Data goes in, predictions are scored by a loss function, an optimizer updates parameters, repeat at massive scale.
- **Inference** = working. A prompt goes in, a response comes out, parameters stay frozen.
- **Parameters** are the model's internal numerical settings — the tuned "knobs" that encode what the model learned.
- **Pretrained** = use as-is. **Fine-tune** = continue training on specific data. **From scratch** = train a new model.
- Every API call you'll ever make is inference. Chatting with a model teaches it nothing.

## Practice questions

Full questions are listed in [practice-questions.md](practice-questions.md).

1. In your own words, what is the difference between training and inference?
2. What does a loss function measure, broadly?
3. Why doesn't a model learn from the conversations people have with it?
4. Your app gives a user a wrong answer. Does retrying the same prompt "teach" the model? Why or why not?
5. Is fine-tuning the same as using a pretrained model? Explain the difference.

## References

- [Google Gemini API documentation](https://ai.google.dev/gemini-api/docs) — hosted models used via inference
- [Hugging Face documentation](https://huggingface.co/docs) — covers models, training, and inference
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) — free course with conceptual depth
