import openai,os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('API_KEY')



print("Chat Bot made by SOHAM RAY")
print("-----------------------------------------")

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

while True:
    message = input("You : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"\nSync Intern ChatBot : {reply} \n")
    messages.append({"role": "assistant", "content": reply})
     




















