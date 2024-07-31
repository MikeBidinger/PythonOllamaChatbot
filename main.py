from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

HIST_LOG = "history.log"
TEMPLATE = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer: 
"""

# Create a LangChain chain using the Ollama LLM
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(TEMPLATE)
chain = prompt | model


def log_history(context: str):
    # Write the conversation history to a file
    with open(HIST_LOG, "w") as f:
        f.write(context)


def conversation_handler(context: str = ""):
    # Conversation loop
    while True:
        # Get the user prompt
        user_input = input("You: ")
        # If the user provided 'exit' as prompt, break out of the conversation loop
        if user_input.lower() == "exit":
            break
        # Invoke the LLM to get a response
        result = chain.invoke({"context": context, "question": user_input})
        print(f"Bot: {result}\n")
        # Append the user prompt and chatbot prompt to the conversation context
        context += f"\nUser: {user_input}\nAI: {result}\n"
        # Log the conversation history to a file
        log_history(context)


if __name__ == "__main__":
    print("\nWelcome to the Python AI Chatbot!")
    print("You can type 'exit' to quit the script.\n")
    conversation_handler()
