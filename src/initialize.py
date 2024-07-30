from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from loader import get_chunks
from vectorstore import get_vectorstore
from retriever import get_retriever_and_prompt

def initialize():
  ollama = Ollama(model="llama3")
  chunks = get_chunks("embeddings/monopoly.pdf")
  vectorstore = get_vectorstore(chunks)
  document_retriever, prompt = get_retriever_and_prompt(vectorstore, ollama)
  rag_chain = ({"context": document_retriever, "question": RunnablePassthrough()} | prompt | ollama | StrOutputParser())
  return rag_chain