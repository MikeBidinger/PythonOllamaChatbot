from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import re
from utils import print_welcome, TEMPLATE, HIST, ERROR_MSG

# Create a pipeline using the LangChain template and the Ollama LLM
prompt = ChatPromptTemplate.from_template(TEMPLATE)
model = OllamaLLM(model="llama3")
chain = prompt | model


def get_response(context: str, user_input: str) -> str:
    # Invoke the LLM to get a response
    try:
        response = chain.invoke({"context": context, "question": user_input})
    except:
        response = ERROR_MSG
    return response


def conversation_handler(context: str = ""):
    # Conversation loop
    while True:
        # Get the user prompt
        user_input = input("You:\t")
        # If the user provided 'exit' as prompt, break out of the conversation loop
        if user_input.lower() == "exit":
            break
        # Get the LLM response for the given input and context
        response = get_response(context, user_input)
        print(f"Bot:\t{response}\n")
        # Append the user and chatbot prompt to the conversation context
        context += f"\nhuman: {user_input}\nai: {response}"
    return context


if __name__ == "__main__":
    print_welcome()
    context = conversation_handler(HIST)
