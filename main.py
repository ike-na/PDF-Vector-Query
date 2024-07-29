import os
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


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
    load_vectorstore = Chroma(persist_directory="chroma_vector_db",
                              embedding_function=OllamaEmbeddings(model="nomic-embed-text"),
                              collection_name="local-rag" )
    print("\nFound chroma_vector_db. \n \n Loaded the vectorstore.\n")
    return load_vectorstore
  else:
    return save_vectorstore(chunks)
  
def get_chunks(path):
  # do here an if else to check if the file exists
  loader = UnstructuredPDFLoader(file_path=path)
  data = loader.load()
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
  chunks = text_splitter.split_documents(data)
  return chunks

def get_retriever(vectorstore, ollama):
    # Query translation in order to improve the retrieval accuracy.
    query_prompt = PromptTemplate(
      input_variables=["question"],
      template="""You are an AI language model assistant. Your task is to create 5 different variations of the original question to help retrieve relevant documents from a vector database. 
      These variations should provide multiple perspectives to overcome limitations of distance-based similarity search. Clearly separate each alternative question with a newline.
      Original question: {question}""")

    retriever = MultiQueryRetriever.from_llm(
        vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5}),
        ollama,
        prompt=query_prompt 
    )

    template = """Answer the following question based on this context: {context}
    Question: {question}"""

    return retriever, ChatPromptTemplate.from_template(template)

def main():
  ollama = Ollama(model="llama3")
  chunks = get_chunks("embeddings/monopoly.pdf")
  vectorstore = get_vectorstore(chunks)

  retriever, prompt = get_retriever(vectorstore, ollama)

  chain = (
      {"context": retriever, "question": RunnablePassthrough()}
      | prompt
      | ollama
      | StrOutputParser()
  )

  question = input("Enter your question: ")

  result = chain.invoke({"question": question})
  print(result)

  # vectorstore.delete_collection() # Uncomment this line to delete the vectorstore


if __name__ == "__main__":
    main()