## Learning Roadmap

This repository follows a progressive path, from Python fundamentals to building real-world applications with backend technologies and AI.

### 01. Python Fundamentals — Current Foundation

| Folder | Topic | Status |
|---|---|---|
| `00-python/` | Introduction to Python | Existing |
| `01-basics/` | Variables, input/output, strings | Existing |
| `02-datatypes/` | Data types and type checking | Existing |
| `03-operators/` | Arithmetic, comparison, logical operators | Existing |
| `04-conditions/` | Conditional statements | Existing |
| `05-match-case/` | Pattern matching | Existing |
| `06-loops/` | Loops and loop control | Existing |
| `07-first-project/` | First complete Python project | Existing |
| `08-functions/` | Functions, parameters, return values | Existing |

### 02. Intermediate Python — Next Stage

Topics that build on the fundamentals and help you write cleaner, more reusable programs.

- **Data Structures:** Lists, tuples, sets, dictionaries, nested collections
- **Strings in Depth:** Formatting, slicing, searching, useful methods
- **Functions in Depth:** Default arguments, keyword arguments, `*args`, `**kwargs`, scope
- **Lambda Functions:** Anonymous functions and when to use them
- **Comprehensions:** List, set, and dictionary comprehensions
- **Functional Tools:** `map()`, `filter()`, `zip()`, `enumerate()`, and an introduction to `functools.reduce()`
- **Recursion:** Base cases, recursive calls, and common pitfalls
- **Built-in Functions:** Useful functions such as `sorted()`, `any()`, `all()`, and `sum()`

### 03. Object-Oriented Programming (OOP)

Learn how to organize programs around objects and classes.

- Classes and objects
- Constructors and the `__init__()` method
- Instance, class, and static methods
- Instance attributes and class attributes
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Composition versus inheritance
- Properties and the `@property` decorator
- Special methods and operator overloading
- Dataclasses
- Practical OOP design and common mistakes

**Possible projects:** Bank Account System, Library Management System, and a small inventory application.

### 04. Advanced Python Concepts

Go deeper into how Python behaves and how to build maintainable programs.

- Iterables, iterators, and generators
- Generator expressions and `yield`
- Decorators
- Closures
- Context managers and the `with` statement
- Exception handling: `try`, `except`, `else`, and `finally`
- Raising custom exceptions
- File handling: text, JSON, and CSV
- Working with paths using `pathlib`
- Modules, imports, and packages
- `__name__ == "__main__"`
- Type hints and annotations
- Docstrings and code organization
- Regular expressions
- Dates, times, and useful standard-library modules

### 05. Python Development Environment

Learn to manage Python projects instead of keeping everything in one script.

- Installing and selecting Python versions
- Virtual environments with `venv`
- Package management with `pip`
- Dependency files such as `requirements.txt`
- Project configuration with `pyproject.toml`
- Environment variables and `.env` files
- Secrets management and `.gitignore`
- Debugging and reading tracebacks
- Logging
- Testing fundamentals with `unittest` or `pytest`
- Code formatting and linting
- Git and GitHub workflows

### 06. Working with APIs and the Web

Learn how Python applications communicate with other systems.

- HTTP fundamentals
- Requests and responses
- JSON serialization and deserialization
- REST APIs
- API keys, authentication, and headers
- Query parameters and status codes
- Timeouts, retries, and error handling
- Synchronous versus asynchronous programming
- `async` and `await`
- Working with external services

**Possible projects:** API-powered weather app, GitHub profile fetcher, and a command-line API client.

### 07. Backend Development with Python

Move from scripts to applications that serve users and manage data.

- FastAPI fundamentals
- Routes and HTTP methods
- Request validation with Pydantic
- Response models
- Dependency injection
- Error handling and middleware
- Authentication and authorization
- SQL fundamentals
- Database integration
- CRUD operations
- Database migrations
- Testing APIs
- Application configuration
- Deployment fundamentals

**Possible projects:** Task Manager API, Notes API, and an authenticated backend application.

### 08. Databases and Data Persistence

Understand how applications store and retrieve information.

- Relational database concepts
- SQL queries and joins
- PostgreSQL fundamentals
- Connecting Python to databases
- SQLAlchemy
- Transactions and constraints
- Database schema design
- Data validation
- Basic caching concepts
- Database security and safe queries

### 09. Concurrency and Performance

Explore how Python handles multiple tasks and larger workloads.

- Processes versus threads
- Threading and multiprocessing
- Asynchronous I/O
- `asyncio`
- Concurrent API requests
- Profiling and benchmarking
- Memory and performance basics
- Queues and background tasks
- When concurrency is useful — and when it isn't

### 10. Data Analysis and Scientific Python

Build the foundation for working with datasets.

- NumPy
- Pandas
- Data cleaning and transformation
- Reading CSV and JSON datasets
- Exploratory data analysis
- Matplotlib
- Basic statistics and probability
- Working with missing data
- Data visualization

### 11. Machine Learning

Move from general Python programming into machine learning.

- Machine learning fundamentals
- Supervised and unsupervised learning
- Training, validation, and test sets
- Regression and classification
- Feature engineering
- Data preprocessing
- Model evaluation and common metrics
- Overfitting and underfitting
- Scikit-learn
- Model persistence and inference
- Basic neural network concepts

**Possible projects:** House Price Predictor, Spam Classifier, and a simple recommendation system.

### 12. Generative AI and LLM Development

Learn to build applications using modern language models, starting with the underlying concepts before adding frameworks.

- Introduction to Generative AI
- Understanding Large Language Models
- Tokens and tokenization
- Next-token prediction
- Training versus inference
- Context windows and model parameters
- Hallucinations and model limitations
- Prompt design and system instructions
- APIs, SDKs, and API-key security
- Gemini API and response streaming
- Conversation history and memory
- Saving conversation history persistently
- Handling quotas, errors, retries, and timeouts
- Exploring Groq, Mistral, DeepSeek, Hugging Face, and OpenRouter
- Embeddings and semantic similarity
- Vector databases
- Retrieval-Augmented Generation (RAG)
- LangChain fundamentals
- LangGraph and agent orchestration
- Tool calling and structured outputs
- Evaluation, privacy, and responsible AI development

**Possible projects:** Mini LLM Assistant, persistent-memory chatbot, document Q&A application, and a research assistant.

### 13. Software Engineering and Production Practices

Develop habits that help projects remain understandable as they grow.

- Clean code and separation of concerns
- SOLID principles and practical design patterns
- Reusable modules and package design
- Testing and test-driven development fundamentals
- Git branching and pull requests
- Documentation and API contracts
- Security fundamentals
- Docker fundamentals
- CI/CD concepts
- Deployment, monitoring, and logging

### 14. Real-World Projects

The final goal is to combine multiple topics into applications rather than learn everything in isolation.

Possible projects include:

- A complete command-line application
- A REST API with authentication and a database
- A data analysis project using a real dataset
- A machine learning application
- An LLM chatbot with persistent memory
- A RAG application that answers questions about documents
- An AI research assistant using tools and background tasks

---

**Learning principle:** each stage builds on the previous one. Topics will be introduced gradually, with separate files, clear explanations, practice exercises, and projects wherever appropriate. The roadmap is a long-term plan; a topic is marked complete only after its material has actually been added.
