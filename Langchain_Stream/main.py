from langchain_openai import ChatOpenAI


model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0.1
)
# Stream the response
for chunk in model.stream(
    "Explain AI in detail"
):
    print(chunk.content,end='',flush=True) # Print each chunk as it's received
