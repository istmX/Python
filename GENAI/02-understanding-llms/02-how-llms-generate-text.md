# 02 — How LLMs Generate Text

## Learning objectives

By the end of this lesson, you should be able to:

- Explain what tokenization means and why models need it
- Describe next-token prediction in your own words
- Explain how text is generated incrementally, one token at a time
- Explain why the prompt and previous context shape the answer
- Describe the role of probabilities in choosing the next token
- Understand that "next-token prediction" is a useful simplification, not the full internal story

## First, the big secret

Here's the thing nobody tells beginners: **an LLM's entire job is to answer one question — "what comes next?"**

That's it. That's the whole trick. Given some text, the model predicts the most likely next piece of text. Then it adds that piece and predicts the one after. And the one after. Until it decides the answer is finished.

Everything else — the chat interface, the personality, the refusal to answer certain questions — is built on top of that simple loop by the application around the model.

Let's open the hood and watch it work.

## Step 1: Tokenization — chopping text into pieces

Computers don't read words. They read numbers. So before any processing happens, your text gets broken into **tokens** — chunks of text the model works with as single units.

A token might be:

- A whole word: `Python`
- Part of a word: `token` + `ization`
- A single character: `z`
- Punctuation, spaces, even emojis

So the sentence:

```
The cat sat
```

might become tokens like:

```
[The] [cat] [sat]
```

and a longer word like `unhappiness` might become:

```
[un] [happ] [iness]
```

**Why not just treat a whole sentence as one unit?** Because sentences are infinite. There are endless ways to arrange words, and almost every sentence you type has never existed before in exactly that form. If the model only ever saw whole sentences, it could never handle anything new.

Tokens are the model's vocabulary — a fixed set of pieces it can work with. Breaking unfamiliar words into smaller known pieces lets the model handle words it has never seen. It's like how you can read a word you've never encountered by sounding out its parts.

The exact token boundaries depend on the model's tokenizer. Don't assume `cat` is always one token everywhere — different models chunk text differently. We'll count what this means for cost in lesson 03.

## Step 2: Next-token prediction — the heart of everything

Once your text is tokens, the model does something deceptively simple:

**It looks at all the tokens so far and predicts which token is most likely to come next.**

Then it appends that token to the sequence and does it again. And again. One token at a time, until the answer is complete.

Watch it work with a tiny example. Suppose the prompt is:

```
The cat sat on the
```

The model considers what could follow. Many continuations are possible — `mat`, `floor`, `couch`, `roof` — and the model assigns each a probability based on patterns it learned during training. In our toy example, the rankings might look like:

| Candidate next token | Illustrative probability |
|---|---|
| `mat` | highest |
| `floor` | lower |
| `couch` | lower still |
| `the` | very low |

These numbers are **illustrative** — a teaching example to show the shape of the idea. They are not the actual internal state of any real model, and real models consider their entire vocabulary at every step, not four candidates.

The model picks one token (more on how in a moment), appends it:

```
The cat sat on the mat
```

...and immediately asks the question again: what comes next? Given this longer context, `mat` makes some continuations more likely and others less likely. The answer grows, token by token, each choice conditioned on everything before it.

![From input text to tokens, through the model, to possible next tokens and continued generation](diagrams/02-next-token-prediction.excalidraw)

**How to read this diagram:**

1. **Input text** enters from the left.
2. **Tokenization** breaks it into manageable pieces.
3. **Model processing** runs the tokens through the trained model.
4. **Possible next tokens** appear as a set of candidates with different likelihoods — visually ranked so you can see some continuations are favored over others.
5. **A token is selected** and appended to the sequence.
6. **The loop continues** — the extended sequence goes back through the model for the next token, and generation proceeds until the model signals it's done.

## Step 3: Where probability comes in

You might wonder: if the model "knows" the most likely next token, why doesn't it always just pick the top one?

It can — that's a valid strategy, and it makes output deterministic and repetitive. But most of the time, applications sample from the probability distribution instead: likelier tokens get picked more often, but less likely ones still get a chance. That's why two runs of the same prompt can produce different answers, and why LLMs have a reputation for being "creative."

This is also why the same question can be answered differently on different days. The answer depends on the prompt, the context, and the sampling — not on a stored script.

## Why the prompt and context shape everything

Because every token is predicted from everything before it, the answer is always a function of:

- **The prompt** — what you actually asked
- **The context** — everything else in the input: system instructions, earlier messages, retrieved documents, whatever the application bundled together

Change the prompt, change the answer. Add context, change the answer. This is why lesson 04 (tokens and context windows) matters so much: the context is not a free resource, and what you include directly shapes what comes out.

## The honest fine print

"Next-token prediction" is the right mental model for a beginner — it explains the behavior you'll observe and it's genuinely how the output loop works. But it is a simplification.

Real models do far more internally: multiple layers of computation, attention mechanisms that weigh which previous tokens matter most, and plenty of other machinery that researchers continue to study and debate. Describing all of that would take us deep into transformer architecture and mathematics — deliberately out of scope for this module.

For now, hold onto this: **the model generates text by repeatedly predicting the next token from the patterns it learned during training.** That model is correct, useful, and enough to understand everything we'll build in the coming lessons.

What you should *not* walk away believing:

- ❌ "The model searches a database of sentences and copies one." It doesn't. It generates new sequences from learned patterns — which is why it can produce text that has never existed before, and why it can also produce fluent nonsense.
- ❌ "The model is certain about its answers." It produces probability distributions, not certainties. High probability is not the same as truth.

## Common misconceptions

**❌ "The model thinks about the whole answer, then writes it down."**
No — it commits to one token at a time, without a plan for the ending. Sometimes this is visible: a model can write itself into a corner because an early token made a good ending unlikely.

**❌ "Tokens are exactly words."**
They're related but not identical. One word can be several tokens, and one token can span parts of several words. Counting tokens ≠ counting words.

**❌ "The most likely token is always the best answer."**
"Most likely according to training patterns" and "most useful or true for you" are different things. The model optimizes for plausible continuation, not for correctness.

## Recap

- Text is broken into **tokens** — sub-word pieces that form the model's vocabulary.
- The model's core job is **next-token prediction**: given the tokens so far, predict what comes next.
- Generation is **incremental**: pick a token, append it, repeat.
- Candidate tokens have **probabilities**; sampling from them introduces variation between runs.
- Every prediction is conditioned on the **prompt and context**, so what you send shapes what you get back.
- Next-token prediction is a simplification — a correct and useful one, but not the complete internal story.

## Practice questions

Full questions are listed in [practice-questions.md](practice-questions.md).

1. Why can't a model just treat each whole sentence as a single unit?
2. In your own words, what is next-token prediction?
3. Why can the same prompt produce different answers on different runs?
4. A classmate says the model "looks up sentences in a big database." How would you correct them, using what you learned today?

## References

- [Google Gemini token documentation](https://ai.google.dev/gemini-api/docs/tokens) — how one major provider explains and counts tokens
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) — conceptual and practical coverage of how models work
