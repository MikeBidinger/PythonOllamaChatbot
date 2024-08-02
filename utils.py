# ------------------------------------------------------------------------------
# chatbot.py
# ------------------------------------------------------------------------------

TEMPLATE = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer: 
"""

HIST = """
human: Peter has 5 pens.
ai: Okay Peter has 5 pens.
human: Peter throws 2 pens away."""

# Example questions for given conversation history:
# - How many pens does Peter now have?

ERROR_MSG = "Oops! Something went wrong. Please try again."


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


# ------------------------------------------------------------------------------
# app.py
# ------------------------------------------------------------------------------


def read_file(file_path: str, encoding: str = None) -> str:
    data = ""
    with open(file_path, "r", encoding=encoding) as f:
        data = f.read()
    return data


# HISTORY = [
#     {"role": "human", "msg": "I will provide some csv data:"},
#     {"role": "human", "msg": read_file("data/data.csv")},
# ]

# HISTORY = [
#     {"role": "human", "msg": "I will provide some markdown data:"},
#     {"role": "human", "msg": read_file("data/data.md")},
# ]

HISTORY = [
    {"role": "human", "msg": "I will provide some text:"},
    {"role": "human", "msg": read_file("data/data.txt")},
]

# Example questions for given conversation history of "data.txt":
# - What are the incomes of Peter?
# - What are the monthly expenses?
# - What is the total amount of potential savings each month?
# - How much a year is saved for Peter's daughter?
# - If Julia turns 14 how much is saved?
