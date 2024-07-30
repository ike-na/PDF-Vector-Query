# RAG-Based PDF Query System

This application is a retrieval-augmented generation (RAG) system with a simple web interface that allows users to upload their PDFs. Once uploaded, the application embeds the documents to a vector database. Users can then interact with the embedded PDFs by making queries, which are processed by a large language model (llama3:8b). This enables users to get answers specific to the content of the documents.

# Technology Stack

- **Backend:** Python with Flask
- **Large Language Model (LLM):** [Ollama3:8b](https://ollama.com/library/llama3:8b)
- **Framework for LLM:** [LangChain](https://python.langchain.com/v0.2/docs/introduction/)
- **Database:** Chroma Vectorstore
- **Frontend:** React with TypeScript
- **Deployment:** Docker, Kubernetes (optional), AWS Cloud

# Learnings

- **Query translation:** Translating the input question in order to improve the retrieval accuracy. This addresses the problem where distance-based similarity search between the query and the documents is affected by ambiguous user input, resulting in poor results.

# Currently working on the front-end!
