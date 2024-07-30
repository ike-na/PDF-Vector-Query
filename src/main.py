from initialize import initialize

def main():
  while True:
    question = input("\nEnter your question or type 'exit' to quit: ")
    if question.lower() == "exit":
      break
    try:
        rag_chain = initialize()  # Faster to initialize than embed each time.
        result = rag_chain.invoke({"question": question})
        print("\n" + result)
    except Exception as e:
        print(f"An error occurred: {e}")
        break
  #vectorstore.delete_collection() # Uncomment this line to delete the vectorstore

if __name__ == "__main__":
    main()