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


def format_response(response: str) -> str:
    # Format the response for better readability
    return response.strip().replace("\n\n", "\n").replace("\n", "\n\t")


def get_response(input: dict) -> str:
    # Invoke the LLM to get a response
    try:
        response = chain.invoke(input)
    except:
        response = "Oops!\nSomething went wrong.\nPlease try again."
    return format_response(response)


def conversation_handler(context: str = "", log: bool = True):
    # Conversation loop
    while True:
        # Get the user prompt
        user_input = input("You:\t")
        # If the user provided 'exit' as prompt, break out of the conversation loop
        if user_input.lower() == "exit":
            break
        # Get the LLM response for the given input and context
        response = get_response({"context": context, "question": user_input})
        print(f"Bot:\t{response}\n")
        # Append the user and chatbot prompt to the conversation context
        context += f"\nUser:\n\t{user_input}\nAI:\n\t{response}\n"
        # Log the conversation history to a file
        if log:
            log_history(context)


if __name__ == "__main__":
    print("\nWelcome to the Python AI Chatbot!")
    print("You can type 'exit' to quit the script.\n")
    conversation_handler()
