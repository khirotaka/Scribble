from langchain.llms import VertexAI
from langchain import ConversationChain

llm = VertexAI(temperature=0)
conversation = ConversationChain(llm=llm)
command = input("You: ")

while True:
    response = conversation.predict(input=command)
    print(f"Vertex: {response}")

    command = input("You: ")
    if command == "exit":
        break
