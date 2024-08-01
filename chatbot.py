from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

HIST_LOG = "history.log"
TEMPLATE = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer: 
"""

# Create a pipeline using the LangChain template, the Ollama LLM and the output parser
prompt = ChatPromptTemplate.from_template(TEMPLATE)
model = OllamaLLM(model="llama3")
parser = StrOutputParser()
chain = prompt | model | parser


def log_history(context: str):
    # Write the conversation history to a file
    with open(HIST_LOG, "w") as f:
        f.write(context)


def format_response(response: str) -> str:
    # Format the response for better readability
    return response.strip().replace("\n\n", "\n").replace("\n", "\n\t")


def get_response(context: str, user_input: str) -> str:
    # Invoke the LLM to get a response
    try:
        response = chain.invoke({"context": context, "question": user_input})
    except:
        response = "Oops! Something went wrong. Please try again."
    return response


def conversation_handler(context: str = "", log: bool = True):
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
        context += f"\nHuman:\n\t{user_input}\nAI:\n\t{response}\n"
        # Log the conversation history to a file
        if log:
            log_history(context)


def print_welcome():
    welcome_text = "Welcome to the Python AI Chatbot!"
    info_text = "You can type 'exit' to quit the script."
    print("")
    for _ in range(80):
        print("-", end="")
    print(f"\n{welcome_text:^80}")
    print(f"{info_text:^80}")
    for _ in range(80):
        print("-", end="")
    print("\n")


if __name__ == "__main__":
    print_welcome()
    conversation_handler(context="""
Human: Peter has 5 pens.
AI: Okay Peter has 5 pens.
Human: Peter throws 2 pens away. How many pens does Peter now have?
AI: That make Peter still has 3 pens.""", log=False)
