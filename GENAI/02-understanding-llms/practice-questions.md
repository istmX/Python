# Practice Questions — Understanding LLMs

Work through these after finishing the lessons. They're designed to check understanding, not memory — if you can answer them in your own words, you've got it.

Attempt everything before scrolling to the [answer key](#answer-key).

## Basic understanding

1. In your own words, what does each word in "Large Language Model" mean?
2. Is every machine learning system an LLM? Is every LLM a machine learning system? Explain both answers.
3. What is tokenization, and why do models need it instead of treating a whole sentence as one unit?
4. What is a context window, and what has to fit inside it?

## Explain in your own words

5. Describe next-token prediction as if you were explaining it to a friend who has never used an AI.
6. Explain the difference between training and inference without using the words "parameters" or "data."
7. Why does a chatbot seem to remember your conversation even though the model itself remembers nothing?

## Scenarios

8. Your friend says, "The chatbot looked up the answer on the internet." Using what you learned, explain what probably happened instead.
9. A classmate insists the model "searches a database of sentences and copies the best match." How do you correct them?
10. You ask a model the same question twice and get two different answers. List two reasons this can happen.
11. A chatbot gives you a detailed, confident answer about a medical symptom that turns out to be wrong. Which concept from lesson 05 explains this, and what should you have done differently?

## Compare and contrast

12. Training vs. fine-tuning vs. using a pretrained model — how do they differ in whether they change the model?
13. Context length vs. persistent memory — what's the difference, and who provides the second one?
14. Model uncertainty vs. missing context vs. outdated information — for each, name one situation where it's the likely cause of a bad answer.

## Diagram interpretation

15. Look at [01-llm-overview.excalidraw](diagrams/01-llm-overview.excalidraw). Describe the journey of a question from keyboard to answer. What did the dashed box represent, and why does it vary between applications?
16. Look at [02-next-token-prediction.excalidraw](diagrams/02-next-token-prediction.excalidraw). Walk through the diagram step by step. Where does the loop happen, and why?
17. Look at [03-training-vs-inference.excalidraw](diagrams/03-training-vs-inference.excalidraw). What is the single biggest structural difference between the two sides?
18. Look at [04-context-window.excalidraw](diagrams/04-context-window.excalidraw). A long conversation starts losing early messages. Using the diagram, explain why that happens.
19. Look at [05-why-llms-hallucinate.excalidraw](diagrams/05-why-llms-hallucinate.excalidraw). Why does the diagram show a verification step as separate from the model? What can that step catch — and what can it still miss?

---

## Answer key

**1.** **Language** — the model works with human language: text in, text out. **Model** — a mathematical system that learned patterns from data. **Large** — enormous: billions of internal settings, trained on vast amounts of text. Together: a very large mathematical system trained on text to predict language.

**2.** No, not every ML system is an LLM — a spam filter or a chess engine is ML (or just classic AI) without being a language model. Yes, every LLM is machine learning: LLMs are deep learning models, which are a subset of ML.

**3.** Tokenization is breaking text into smaller pieces (tokens) that the model processes as units. Sentences can't be single units because there are infinitely many unique sentences — the model would never handle a new one. Tokens give the model a fixed vocabulary and let it handle unseen words by breaking them into known pieces.

**4.** A context window is the maximum amount of text (in tokens) a model accepts in a single request. Everything must fit inside it: system instructions, conversation history, your current message, and the generated response.

**5.** *(Own words expected.)* The model reads the text so far and predicts the most likely next piece. It appends that piece and predicts the next one, over and over, until the answer is complete. Each prediction depends on everything before it.

**6.** *(Own words expected.)* One phase is when the system learns from examples, changing itself to get better. The other is when the finished system is used to produce answers without changing at all.

**7.** The application stores the conversation history and sends it back with every new message. The model "remembers" only because it's being shown the history each time — the model itself keeps nothing between requests.

**8.** A standard LLM API call doesn't browse the web. The model generated the response from patterns learned during training, token by token. (If the app has a web search feature, the *application* searched — not the model.)

**9.** The model has no database of sentences. It generates each response from learned statistical patterns, predicting one token at a time. That's why it can produce text that has never existed before — and fluent fiction that sounds like a real answer.

**10.** Any two of: probability-based sampling means the same prompt can pick different tokens; the exact prompt phrasing changes the output; generation has inherent run-to-run variation.

**11.** Hallucination — a confident, plausible, unsupported answer (lesson 05). You should have verified the claim against a trusted source, especially for high-stakes topics like health, and treated the output as a draft to check, not a final word.

**12.** Training from scratch builds a new model and updates its parameters. Fine-tuning takes an existing pretrained model and continues training it on specific data — it also updates parameters, but in a targeted way. Using a pretrained model (e.g., an API call) doesn't update anything — it's pure inference.

**13.** Context length is the per-request token limit — everything the model can see right now. Persistent memory is long-term storage the *application* maintains around the model (databases, history files) and injects into requests. The model provides only the first; the app must provide the second.

**14.** **Uncertainty** — the model has weak patterns for a niche topic. **Missing context** — the answer needed information you didn't include in the prompt. **Outdated information** — the model's training data ended before the event. Each has a different fix: rephrase/use a better model, add context, or provide retrieval.

**15.** The question flows: user input → AI application (which packages it with history and instructions) → LLM → generated response → user. The dashed box is the application's extra layer — safety checks, retrieval, tools, post-processing — and it varies because every product builds this layer differently.

**16.** Input text → tokenization → model processing → candidate tokens with different probabilities → one token selected → appended to the sequence. The loop is the arrow back: the extended sequence goes through the model again for the next token. Generation continues until the model signals completion.

**17.** Training has an update loop — predictions are scored (loss) and an optimizer changes the parameters, over and over. Inference has no loop: the prompt goes in, the response comes out, and the parameters stay frozen.

**18.** The conversation history consumes the finite context window. When the window fills up, the application must drop, summarize, or window the old messages — so early content is no longer in the request, and the model can't "see" it anymore.

**19.** The verification step is separate because the model's job ends at generating plausible text — checking facts against sources is a different job, done by retrieval, tooling, or humans. It can catch fabricated claims and unsupported statements. It can still miss errors: a plausible misreading of a good source, a bad trusted source, or a subtle factual slip that passes the check.
