# Sequential langchain example that:
#  1. interprets the question, converting it into a math problem
#  2. uses the LLMMathChain to solve the math problem
# Note, this is far more accurate than just asking GPT direcly
#
# Examples:
#  python .\langchain\sequential-math-example.py "If I had five dollars for every goal scored in the 2018 soccer world cup final, how much money would I have?"
#  python .\langchain\sequential-math-example.py "If the letter A is worth 3 points, and the letter B is worth 9 points, but every other letter is worth 2 points how many points is the word abracadabra?"

import os
import sys
from langchain.llms import OpenAI
from langchain.chains import LLMChain, LLMMathChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate

if len(sys.argv) < 2:
    print("Please provide the question as a command line argument.")
    sys.exit(1)
question = sys.argv[1]

# get the API key from the .env file
os.environ['OPENAI_API_KEY'] = open('.env').readline().strip()

llm = OpenAI(temperature=0.02)
template = """You are a very good mathematician who is trained to convert a math question into a math problem that can be given to a calculator
You do not solve the question. Rather you look up the required information, then turn it into a simple math problem.
Here are some examples:

Question: If I am five years old now, how old will I be in 12 years?
What is 5 + 12?

Question: What does a 12% tip on a $45.00 bill come out to?
What is 45 * 0.12?

Question: What does 3 liters of water weigh on the moon?
What is 3 * 1.62?

Question: How many more players are in a baseball team than a basketball team?
What is 9 - 5?

Question: {input}"""

prompt = PromptTemplate(template=template, input_variables=["input"])
interpretation_chain = LLMChain(prompt=prompt, llm=llm)

math_llm = LLMMathChain.from_llm(llm, verbose=True)

overall_chain = SimpleSequentialChain(chains=[interpretation_chain, math_llm], verbose=True)

print(overall_chain.run(question))