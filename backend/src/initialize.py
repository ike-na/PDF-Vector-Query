from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from src.loader import get_chunks
from src.vectorstore import get_vectorstore
from src.retriever import get_retriever_and_prompt

def initialize(pdf_path):
    ollama = Ollama(model="llama3")
    chunks = get_chunks(pdf_path)  # Use the provided file path
    vectorstore = get_vectorstore(chunks)
    document_retriever, prompt = get_retriever_and_prompt(vectorstore, ollama)
    rag_chain = ({"context": document_retriever, "question": RunnablePassthrough()} | prompt | ollama | StrOutputParser())
    return rag_chain