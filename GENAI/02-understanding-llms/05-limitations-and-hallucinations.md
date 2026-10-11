# 05 — Limitations and Hallucinations

## Learning objectives

By the end of this lesson, you should be able to:

- Explain what an AI hallucination is
- Explain why a model can generate a plausible but incorrect answer
- Explain why fluent language is not proof of factual correctness
- Distinguish between model uncertainty, missing context, outdated information, and factual error
- Explain why models can produce different answers to similar prompts
- Explain how grounding, retrieval, source verification, and evaluation can reduce errors
- Explain why these techniques don't guarantee perfect accuracy
- Explain why human judgment still matters in consequential situations

## The confident wrong answer

It's happened to all of us. You ask an AI something specific, and it responds instantly, smoothly, and completely wrong — citing a source that doesn't exist, a law that was repealed, or a library function that was never released. No hedging. No uncertainty. Just pure, fluent confidence.

That's a **hallucination**: a generated response that is confident and plausible-sounding but unsupported by fact.

Hallucinations aren't a bug in the sense of a typo. They're a direct consequence of how the model works. Remember lesson 02: the model predicts what text *should* come next based on patterns. It's optimizing for plausible continuation, not for truth. When the training patterns point toward a confident-sounding answer, the model produces one — whether or not it's correct.

## Why does this happen?

Let's be precise about the mechanism, because the wrong explanation leads to the wrong fixes.

The model doesn't have a fact database with a "verified" column. It has learned statistical patterns about how words, facts, and explanations tend to appear together. Several things can go wrong:

- **The pattern itself is wrong.** If incorrect claims appeared frequently in training data, the model may reproduce them fluently.
- **The model "fills in a gap."** Asked about something it has little reliable pattern for, it still generates *something* — models are strongly biased toward producing an answer rather than none.
- **Confidence and correctness are different things.** The model's sampling process favors likely-sounding text, and likely-sounding text reads as confident. Fluency is a language property; accuracy is a fact property. They correlate loosely, if at all.

The uncomfortable takeaway: **fluent language is not proof of factual correctness.** A beautifully written answer can be total fiction, and a hedged, uncertain answer can be exactly right. You have to check, not vibe.

## Not all errors are the same

When a model gets something wrong, it helps to know *why*, because the fixes differ:

| Cause | What it looks like | What helps |
|---|---|---|
| **Model uncertainty** | The model genuinely doesn't know or has weak patterns for the topic | Asking for sources, rephrasing, using a more capable model |
| **Missing context** | The answer needs information you didn't provide | Supplying the relevant context in the prompt |
| **Outdated information** | The model's training data ended before the event | Retrieval / web search to ground the answer in current data |
| **Factual error** | The model states something false with confidence | Source verification, grounding, human review |

These can look identical from the outside — a wrong answer is a wrong answer — but they have different causes and different remedies.

## Why similar prompts get different answers

Between the probability-based generation (lesson 02), the sensitivity of the output to the exact prompt, and any non-determinism in sampling, the same question asked twice can produce different answers. Add slight rephrasing and the differences can grow.

This is normal. It doesn't mean the model is "thinking differently" — it means the generation process has inherent variability. It's another reason not to treat any single output as settled truth.

## What can reduce errors (and what can't)

The good news: the field has developed techniques that genuinely help. The bad news: none of them are magic.

- **Grounding** — giving the model a trusted source of facts to work from, so it answers from evidence instead of pure pattern-matching.
- **Retrieval** — fetching relevant documents (manuals, databases, current web results) and including them in the context, so the answer is anchored to real sources. You'll see this called RAG (Retrieval-Augmented Generation) in lesson 12.
- **Source verification** — checking the model's claims against the retrieved sources, or requiring the model to cite where each claim came from.
- **Evaluation** — systematically testing the model's outputs to find failure modes and measure improvement.

These techniques reduce certain categories of errors — especially "made up facts" and "out of date facts" — and they make systems more trustworthy. But they do **not** guarantee perfect accuracy. A model can misread a retrieved document, over-trust a bad source, or produce a subtly wrong synthesis of good sources. Verification steps can also miss errors, especially plausible ones.

Treat these techniques as risk reduction, not truth machines.

## Why human judgment still matters

Put it all together: the model can be confidently wrong, its knowledge has an edge, its output varies run to run, and our best techniques only reduce (not eliminate) errors.

The conclusion isn't "never trust AI." It's **calibrate your trust to the stakes.**

- Low stakes — brainstorming names, drafting an email, explaining a concept: use the output freely, skim it, move on.
- Medium stakes — code that will run, a summary people will read: verify the important parts, test the code, spot-check the facts.
- High stakes — medical, legal, financial, safety-critical decisions: the model's output is a draft for a qualified human, never the final word.

The model is a tool that writes like an expert. Your job is to think like one.

## Common misconceptions

**❌ "If it sounds confident and detailed, it's probably right."**
Confidence is a language pattern, not a truth signal. Detailed wrong answers are often the most convincing ones.

**❌ "Hallucinations mean the model is broken."**
They're an inherent property of prediction-based generation. Even the best models hallucinate.

**❌ "Retrieval makes the model always correct."**
Retrieval grounds the answer in sources, but the model can still misread, mis-synthesize, or over-trust them.

**❌ "Only weak models hallucinate."**
All models do. Better models hallucinate less and more subtly — which can make their errors harder to catch.

## Recap

- A **hallucination** is a confident, plausible, unsupported answer.
- It happens because the model predicts plausible text, not verified facts.
- Fluency ≠ correctness. Always verify important claims.
- Errors have different causes: uncertainty, missing context, outdated info, factual error — each with different remedies.
- Grounding, retrieval, source verification, and evaluation reduce errors but never eliminate them.
- Match your trust to the stakes. High-stakes decisions need human judgment.

## Practice questions

Full questions are listed in [practice-questions.md](practice-questions.md).

1. In your own words, what is a hallucination?
2. Why can a model produce a fluent, confident, completely wrong answer?
3. "The model gave a very detailed answer, so it must be accurate." What's wrong with this reasoning?
4. Name two techniques that can reduce hallucinations, and one limitation of each.
5. A friend uses an unverified AI answer for a medical question. Using this lesson, what would you tell them?

## References

- [Google Gemini API documentation](https://ai.google.dev/gemini-api/docs) — grounding features that connect models to trusted sources
- [OpenAI Platform documentation](https://platform.openai.com/docs) — model behavior and limitations
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) — conceptual foundations including model limitations
