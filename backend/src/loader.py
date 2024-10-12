import os
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
  
def get_chunks(path):
  if not os.path.exists(path):
    raise FileNotFoundError(f"File '{path}' not found.")
  pdf_loader = UnstructuredPDFLoader(file_path=path)
  document_data = pdf_loader.load()
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
  chunks = text_splitter.split_documents(document_data)
  return chunks