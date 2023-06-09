# To call this script, use:
#  python have-a-chat.py
#  The script will continue to ask for questions until you press enter without typing anything.

import openai
import sys

openai.api_key_path = '.env'

messages=[
        {"role": "system", "content": "You are a helpful assistant who responds with short answers to questions."}
    ]

print("\033[92m", end="")
print("Hi! I'm your friendly, helpful (gpt-3.5-turbo) AI assistant. Ask a question or press enter to quit.")
print("\033[0m", end="")

while True:
    question = input("> ")
    if not question:
        break

    # add user question to messages list
    messages.append({"role": "user", "content": question})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # change the text color to green
    print("\033[92m", end="")
    print(completion.choices[0].message.content)
    # change the text color back to the default
    print("\033[0m", end="")
    # add completion message to messages list
    messages.append(completion.choices[0].message)