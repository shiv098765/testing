from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

while True:
    user_input =input('YOU: ')
    if user_input == "exit":
        break
    rst=model.invoke(user_input)
    print("AI: ",rst.content)

  