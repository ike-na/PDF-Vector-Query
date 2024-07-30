import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

def save_vectorstore(chunks):
  vectorstore = Chroma.from_documents(
    documents=chunks, 
    embedding=OllamaEmbeddings(model="nomic-embed-text",show_progress=True),
    collection_name="local-rag",
    persist_directory="chroma_vector_db"
)
  print("\nSaved vectorstore to chroma_vector_db.\n")
  return vectorstore

def get_vectorstore(chunks):
  if os.path.exists("chroma_vector_db"):
    loaded_vectorstore = Chroma(persist_directory="chroma_vector_db",
                              embedding_function=OllamaEmbeddings(model="nomic-embed-text"),
                              collection_name="local-rag" )
    print("\nFound chroma_vector_db. \n \n Loaded the vectorstore.\n")
    return loaded_vectorstore
  else:
    return save_vectorstore(chunks)