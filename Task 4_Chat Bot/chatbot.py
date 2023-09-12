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
     





























# import openai

# openai.api_key = "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"

# model_engine = "text-davinci-003"
# prompt = "Who is Prime Minister of India ?"

# complete = openai.Completion.create(
#     engine = model_engine,
#     prompt = prompt,
#     max_tokens = 1024,
#     n = 1,
#     stop = None,
#     temperature = 0.5,
# )

# response = complete.choices[0].text
# print(response)



