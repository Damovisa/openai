# To call this script, use:
#  python answer-a-question.py <question>
#  The question should be in quotes.

import openai
import sys

openai.api_key_path = '.env'

if len(sys.argv) < 2:
    print("Please provide the question as a command line argument.")
    sys.exit(1)

question = sys.argv[1]

import openai

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant who responds with short answers to questions."},
        {"role": "user", "content": question}
    ]
)

print(completion.choices[0].message.content)