# RAG-Based PDF Query System

This application is a retrieval-augmented generation (RAG) system with a simple web interface that allows users to upload their PDFs. Once uploaded, the application embeds the documents to a vector database. Users can then interact with the embedded PDFs by making queries, which are processed by a large language model (llama3:8b). This enables users to get answers specific to the content of the documents.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)


# How to Use
Here, I uploaded a Monopoly manual through the web UI and asked the application, "How can I get out of the jail?"

I recorded the videos using `Win + Alt + R`, so the selection process for `monopoly.pdf` in the file explorer isn't visible.

https://github.com/user-attachments/assets/9edad0d2-db73-46f6-83dd-5aa559deec05

https://github.com/user-attachments/assets/09ba0b99-fb9b-4bd5-b605-b7662e0f92f5

https://github.com/user-attachments/assets/ee8c443b-e49a-4c7b-a440-bfade151b135

# Technology Stack

- **Backend:** Python with Flask
  - _Utilizes Flask for building RESTful APIs._
  - _Handles file uploads and data management._
  - _Interacts with Chroma vector database for storage and retrieval._
- **Large Language Model (LLM):** [Ollama3:8b](https://ollama.com/library/llama3:8b)
  - _Implements advanced natural language processing (NLP) capabilities for document interaction._
- **Framework for LLM:** [LangChain](https://python.langchain.com/v0.2/docs/introduction/)
- **Database:** Chroma Vectorstore
  - _Efficient storage and retrieval of vector data._
- **Frontend:** React with TypeScript
- **Deployment:** Docker, Kubernetes (optional), AWS Cloud
  - _Under development._

# Learnings

- **Query translation:** Translating the input question in order to improve the retrieval accuracy. This addresses the problem where distance-based similarity search between the query and the documents is affected by ambiguous user input, resulting in poor results.

- **Document embedding:** Converting documents into vector embeddings to represent their semantic content. This enables similarity searches by comparing vectors, allowing the retrieval of contextually related documents.

- **Vector databases for LLMs:** Understanding the benefits of using vector databases for storing and querying large language model embeddings. Vector databases enhance retrieval efficiency and accuracy in similarity searches, making them particularly useful in handling high-dimensional data from LLMs.

- **Integrating language models:** Gained experience implementing a local LLM as part of a Retrieval-Augmented Generation (RAG) application.

- **Building APIs:** Improved proficiency in creating RESTful APIs with Flask for smooth frontend-backend communication.

- **Frontend development:** Built user interfaces in React and TypeScript, focusing on component design, state management, and responsive layouts.


# Currently working on the Deployment!
