
from langchain_community.llms.ollama import Ollama

model = Ollama(model="mistral")
response_text = model.invoke("hello")

print(response_text)
