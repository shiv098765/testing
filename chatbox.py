from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from playsound import playsound

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history = [
    SystemMessage(content='You are a helpful assistant')
]

while True:
    user_input = input('YOU: ')
    chat_history.append(HumanMessage(content=user_input) )
    if user_input == 'exit':
        break
    rst = model.invoke(user_input)
    chat_history.append(AIMessage(content=rst.content))
    print("AI: ",rst.content)



print(chat_history)    