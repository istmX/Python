# Resources — Understanding LLMs

A curated list of verified, relevant resources for this module. Every link was checked to lead to the documentation or course material described.

Prefer official documentation for technical claims. Use the educational courses and guides to build intuition.

## Official provider documentation

| Resource | Why it's useful |
|---|---|
| [Google Gemini API documentation](https://ai.google.dev/gemini-api/docs) | Official overview of hosted models, their capabilities, and how they're used |
| [Google Gemini token documentation](https://ai.google.dev/gemini-api/docs/tokens) | How one major provider counts and explains tokens — directly supports lesson 02 |
| [Google Gemini API key guidance](https://ai.google.dev/gemini-api/docs/api-key) | How API access is authenticated — context for later coding lessons |
| [OpenAI Platform documentation](https://platform.openai.com/docs) | Official docs: model reference, context limits, API behavior |
| [Hugging Face documentation](https://huggingface.co/docs) | Broad documentation covering models, training, inference, and deployment |

## Courses and structured learning

| Resource | Why it's useful |
|---|---|
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) | Free course that takes you from transformer basics to fine-tuning, with code — excellent next step after this module |
| [Python documentation](https://docs.python.org/3/) | Keep your Python fundamentals sharp — you'll need them when we start coding |

## Diagrams

Every diagram in this module is a native, editable Excalidraw file:

- [01-llm-overview.excalidraw](diagrams/01-llm-overview.excalidraw) — user, application, model, response
- [02-next-token-prediction.excalidraw](diagrams/02-next-token-prediction.excalidraw) — tokenization and the generation loop
- [03-training-vs-inference.excalidraw](diagrams/03-training-vs-inference.excalidraw) — the two phases side by side
- [04-context-window.excalidraw](diagrams/04-context-window.excalidraw) — what fits inside one request
- [05-why-llms-hallucinate.excalidraw](diagrams/05-why-llms-hallucinate.excalidraw) — plausible vs. verified

**How to open a diagram:** drag the `.excalidraw` file onto [excalidraw.com](https://excalidraw.com/), or use the Excalidraw app/extension. The files are plain editable scenes — every box, label, and arrow can be moved and restyled.

## Notes on accuracy

- Model limits, pricing, and capabilities change often. Always check the current documentation for the specific model you plan to use.
- Provider-specific behavior (token counting, context limits, message formats) is not universal across all models and APIs.
- The diagrams in this module are teaching aids. They show conceptual relationships, not internal model architecture.

---

**Maintained by Aryan | ISTMX**

Learning in public, one concept at a time.
