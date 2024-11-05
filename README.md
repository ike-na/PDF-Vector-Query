# RAG-Based PDF Query System

This application is a retrieval-augmented generation (RAG) system with a simple web interface that allows users to upload their PDFs. Once uploaded, the application embeds the documents to a vector database. Users can then interact with the embedded PDFs by making queries, which are processed by a large language model (llama3:8b). This enables users to get answers specific to the content of the documents.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

# Technology Stack

- **Backend:** Python with Flask
  - _Utilizes Flask for building RESTful APIs._
  - _Handles file uploads and data management._
  - _Interacts with Chroma vector database for storage and retrieval._
- **Large Language Model (LLM):** [Ollama3:8b](https://ollama.com/library/llama3:8b)
  - _Implements advanced NLP capabilities for document interaction._
- **Framework for LLM:** [LangChain](https://python.langchain.com/v0.2/docs/introduction/)
- **Database:** Chroma Vectorstore
  - _Efficient storage and retrieval of vector data._
- **Frontend:** React with TypeScript
- **Deployment:** Docker, Kubernetes (optional), AWS Cloud
  - _Under development._

# Learnings

- **Query translation:** Translating the input question in order to improve the retrieval accuracy. This addresses the problem where distance-based similarity search between the query and the documents is affected by ambiguous user input, resulting in poor results.

- **Data retrieval:** Learned how to efficiently pull relevant information from a dataset. This includes understanding search algorithms and how they impact the accuracy and speed of retrieving information.

- **Integrating language models:** Gained skills in working with language models and understanding how to process and generate natural language responses. This involves knowing how to connect the model with user queries to provide meaningful outputs.

- **Building APIs:** Enhanced my ability to create RESTful APIs with Flask, handling requests and responses for frontend-backend communication.

- **Frontend development:** Gained experience in building user interfaces using React and TypeScript. Component design, state management, and creating responsive layouts.

# Currently working on the Deployment!
