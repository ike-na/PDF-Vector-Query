from langchain_core.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.retrievers.multi_query import MultiQueryRetriever


def get_retriever_and_prompt(vectorstore, ollama):
    # Query translation in order to improve the retrieval accuracy.
    prompt_template = PromptTemplate(
      input_variables=["question"],
      template="""You are an AI language model assistant. Your task is to create 5 different variations of the original question to help retrieve relevant documents from a vector database. 
      These variations should provide multiple perspectives to overcome limitations of distance-based similarity search. Clearly separate each alternative question with a newline.
      Original question: {question}""") # The template is close to the MultiQueryRetriever DEFAULT_QUERY_PROMPT

    document_retriever = MultiQueryRetriever.from_llm(
        vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5}),
        ollama,
        prompt=prompt_template 
    )

    answer_template = """Answer clearly to the following question based on this context: {context}
    Question: {question}"""

    return document_retriever, ChatPromptTemplate.from_template(answer_template)