from langchain.llms import VertexAI


llm = VertexAI(model_name="text-bison@001", temperature=0.7)
question = "金曜日の次は何曜日ですか？"
ans = llm(question)

print(ans)