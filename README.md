# Python AI Chatbot GUI using Ollama

This Python AI Chatbot will run locally, so you don't need to pay for a
subscription or connect to a API (like OpenAI), by using
[Ollama](https://ollama.com/).

Used resources:

| Resource                                                                                                                                                                        | Functionality                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| [Tech With Tim](https://www.youtube.com/@TechWithTim) - [Create a LOCAL Python AI Chatbot In Minutes Using Ollama](https://www.youtube.com/watch?v=d0o89z134CQ)                 | LLM (Python)                     |
| [CodingNepal](https://www.codingnepalweb.com/) - [How to Create Working Chatbot in HTML CSS and JavaScript](https://www.codingnepalweb.com/create-chatbot-html-css-javascript/) | Web GUI (HTML, CSS & JavaScript) |
| [Tech With Tim](https://www.youtube.com/@TechWithTim) - [Python Website Full Tutorial](https://www.youtube.com/watch?v=dam0GPOAvVI)                                             | Flask                            |

https://www.youtube.com/watch?v=70H_7C0kMbI&t=400s

## To-Do:

-   Inject given context to the LLM
-   Create GUI App with Flask (HTML, CCS & JavaScript)

## Installation

Start by downloading Ollama from there download page
([Download Ollama](https://ollama.com/download)).

After downloading Ollama, install the App.

Now you're able to check if Ollama is running on your computer by typing in the
command `ollama`.

## Ollama

Ollama is a software that allows us to download and run open source LLM's
(Large Language Models) locally on our computers. For more info visit there
[website](https://ollama.com/) or [GitHub](https://github.com/ollama/ollama).
There are a lot of different models that can be downloaded and ran, but the
larger the model is the more difficult it is to run on your computer.

> [!NOTE]
> You should have at least 8 GB of RAM available to run the 7B models, 16 GB to
> run the 13B models, and 32 GB to run the 33B models.

## Python AI Chatbot

### Setup the LLM

For this specific example script, I will use the Llama 3 model (a relatively
small model of 8B parameters). To download this on our computer we need to
download it by using the following command `ollama pull llama3`.

After downloading, we can test this model by running the following command
`ollama run llama3`. Now the model is running, we are able to type in a message
and get a response in return. To quit the model, use the following command
`/bye`.

### Setup the Virtual Environment

For this specific example script, I use the package manager
[Anaconda](https://www.anaconda.com/) for setting up the virtual environment to
run this script. For additional info and use see my
[Python Anaconda](https://github.com/MikeBidinger/Python_Anaconda) repo.

To create the virtual environment using Anaconda, use the command
`conda create --name [ENV_NAME] python=3.11`. Now the virtual environment is
created, we can activate it using the command `activate [ENV_NAME]`.

> [!NOTE]
> The `[ENV_NAME]` has to be given a appropriate environment name. For this
> specific example script, I used the name `OllamaEnv`.

Now we can install the packages we need to run this example script:

| Package                                     | Anaconda Command                                                                                                     |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [Ollama](https://ollama.com/)               | `pip install ollama` or `conda install ollama -c conda-forge`                                                        |
| [LangChain](https://www.langchain.com/)     | `pip install langchain` or `conda install langchain -c conda-forge`                                                  |
| LangChain-Ollama                            | `pip install langchain-ollama` (no anaconda channel providing the package langchain-ollama at the moment of writing) |
| [Flask](https://flask.palletsprojects.com/) | `pip install flask` or `conda install flask`                                                                         |

### Run the Python AI Chatbot GUI

Now the setup is completed, we are able to run the script within the created
virtual environment.
