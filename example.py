from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3")

response = model.invoke(input="hello world")

print(response)
