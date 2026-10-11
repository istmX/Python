# Python Practice Repository

<p align="center">
  <img src="https://img.shields.io/badge/Python-Learning%20%26%20Practice-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Generative%20AI-LLM%20Learning-8B5CF6?style=for-the-badge" alt="Generative AI" />
  <img src="https://img.shields.io/badge/Projects-Learning%20by%20Building-16A34A?style=for-the-badge" alt="Learning by building" />
</p>

<p align="center">
  <b>From Python fundamentals to building AI-powered applications.</b>
  <br />
  A growing collection of notes, examples, practice programs, and projects.
</p>

---

## Welcome!

This repository is my Python learning and practice space, created to document concepts, experiment with code, and build a solid foundation for software development and AI engineering.

It covers Python from the fundamentals through more advanced language features, with a separate learning path for Generative AI and Large Language Models (LLMs).

You'll find individual topic folders, commented code examples, explanations, exercises, diagrams, reference links, and projects that bring concepts together.

The goal isn't just to make code run. It's to understand how it works, why it works, and how to use that knowledge to build something useful.

## What's inside?

- **Python Fundamentals:** From introductory concepts to functions and core programming logic.
- **Intermediate Python:** Lambda functions, scope, recursion, comprehensions, and functional programming tools.
- **Object-Oriented Programming:** Classes, objects, and the principles of OOP.
- **Advanced Language Features:** Modules, packages, exceptions, file handling, iterators, generators, and built-in functions.
- **Practice and Projects:** Small programs and a multi-file capstone project.
- **Generative AI:** Conceptual lessons about LLMs, how they generate text, context windows, and hallucinations.
- **AI Development:** A Gemini-powered assistant exploring API integration, streaming, and conversation history.

## Repository structure

```text
Python/
├── basic-python/
│   ├── 00-Python/
│   ├── 01-basics/
│   ├── 02-datatypes/
│   ├── 03-operators/
│   ├── 04-conditions/
│   ├── 05-match-case/
│   ├── 06-loops/
│   ├── 07-mini-ai-assistant/
│   ├── 08-functions/
│   ├── 09-lambda-functions/
│   ├── 10-python-scope/
│   ├── 11-recursion/
│   ├── 12-comprehensions/
│   ├── 13-functional-programming/
│   ├── 14-object-oriented-programming/
│   ├── 15-modules-and-packages/
│   ├── 16-exception-handling/
│   ├── 17-file-handling/
│   ├── 18-iterators-and-generators/
│   ├── 19-builtin-functions/
│   └── 20-final-capstone-project/
│
└── GENAI/
    ├── 01-introduction-to-genai/
    └── 02-understanding-llms/
```

Each directory focuses on a particular topic or project. Individual folders contain their own explanations and learning materials.

## Python curriculum

The `basic-python/` directory covers the core Python learning path.

| Folder | Topic | What you'll learn |
|---|---|---|
| `00-Python/` | Introduction to Python | Python basics, characteristics, execution, and getting started |
| `01-basics/` | Basics | Variables, input/output, strings, and type conversion |
| `02-datatypes/` | Data Types | Numbers, strings, booleans, and working with data |
| `03-operators/` | Operators | Arithmetic, comparison, and logical operations |
| `04-conditions/` | Conditions | Decision-making with `if`, `elif`, and `else` |
| `05-match-case/` | Match Case | Pattern matching and choice-driven logic |
| `06-loops/` | Loops | Iteration, `range()`, `break`, and `continue` |
| `07-mini-ai-assistant/` | Mini AI Assistant | Applying Python to an AI-powered application |
| `08-functions/` | Functions | Parameters, arguments, return values, and reusable code |
| `09-lambda-functions/` | Lambda Functions | Small anonymous functions |
| `10-python-scope/` | Scope | Local and global scope and variable visibility |
| `11-recursion/` | Recursion | Functions that call themselves and their base cases |
| `12-comprehensions/` | Comprehensions | Concise ways to construct collections |
| `13-functional-programming/` | Functional Programming | `map()`, `filter()`, `reduce()`, and related concepts |
| `14-object-oriented-programming/` | OOP | Classes, objects, and object-oriented design |
| `15-modules-and-packages/` | Modules and Packages | Organizing and importing reusable code |
| `16-exception-handling/` | Exception Handling | Handling errors and managing exceptional cases |
| `17-file-handling/` | File Handling | Reading and writing files |
| `18-iterators-and-generators/` | Iterators and Generators | Iteration protocols, generators, and `yield` |
| `19-builtin-functions/` | Built-in Functions | Useful functions provided by Python |
| `20-final-capstone-project/` | Final Capstone | Combining multiple concepts into a larger project |

## Generative AI

The `GENAI/` directory focuses on understanding Generative AI and the concepts behind LLM-powered applications.

### `01-introduction-to-genai/`

Introduces Generative AI, what it can do, and how it differs from traditional AI approaches.

### `02-understanding-llms/`

Explores the fundamentals of Large Language Models through separate lessons, practice questions, references, and editable Excalidraw diagrams.

Topics include:

- What an LLM is
- How next-token prediction works
- Training versus inference
- Model parameters and context windows
- Limitations and hallucinations

The learning path emphasizes conceptual understanding before moving deeper into API integrations and AI frameworks.

## Projects

### Mini AI Assistant

The `basic-python/07-mini-ai-assistant/` folder contains a small Gemini-powered assistant that demonstrates how Python can communicate with a language model.

It explores:

- Connecting to the Gemini API using Google's Python SDK
- Reading API keys from environment variables
- Sending prompts to an LLM
- Streaming responses into the terminal
- Maintaining conversation history during a running session

This project introduces practical AI development while keeping the implementation approachable.

### Final Capstone Project

The `basic-python/20-final-capstone-project/` folder brings together concepts from the Python curriculum in a larger, multi-file project.

It demonstrates how individual language features can work together in a more organized application.

Other practice programs throughout the repository help reinforce concepts as they're introduced.

## Getting started

### Requirements

- Python installed on your system
- A code editor or terminal
- Any additional dependencies required by a particular project

Clone the repository:

```bash
git clone https://github.com/istmX/Python.git
cd Python
```

Run an individual Python file:

```bash
python filename.py
```

Depending on your environment, you may need to use `python3` instead.

### Running projects

Some projects require extra packages, environment variables, or external API access. Check the instructions in the relevant folder before running them.

For the Gemini assistant, configure the required API key in a `.env` file and follow the project's setup instructions.

**Security note:** Never commit API keys, credentials, or your `.env` file to GitHub.

## Learning resources

- [Official Python Documentation](https://docs.python.org/3/)
- [The Python Tutorial](https://docs.python.org/3/tutorial/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Google Gen AI Python SDK](https://googleapis.github.io/python-genai/)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)

These resources complement the repository's examples and explanations, providing official references for Python and AI development.

## Repository philosophy

- **Understand before memorizing.** Learn why a feature exists and when to use it.
- **Keep topics organized.** Separate files and folders make concepts easier to revisit.
- **Learn by building.** Practice programs and projects connect theory to implementation.
- **Use reliable references.** Official documentation helps verify details and explore topics further.
- **Keep improving.** Learning materials and projects can evolve as understanding deepens.

## About

**Aryan — Developer and Maintainer**

I'm an AI/ML student interested in Python, software development, and building AI-powered applications.

This repository documents my learning and experimentation across Python programming and Generative AI.

- GitHub: [@istmX](https://github.com/istmX)
- Email: roaringmoon07@gmail.com

---

<p align="center">
  <b>Learn the fundamentals. Understand the concepts. Build real things.</b>
  <br />
  <i>One concept at a time, one project at a time.</i>
  <br /><br />
  © 2026 Aryan
</p>
