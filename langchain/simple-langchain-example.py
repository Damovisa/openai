# Simple question answering, but it uses prompts and langchains instead of calling the OpenAI completions API directly.

import sys
import os
from langchain.llms import OpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

if len(sys.argv) < 2:
    print("Please provide the question as a command line argument.")
    sys.exit(1)
question = sys.argv[1]

# get the API key from the .env file
os.environ['OPENAI_API_KEY'] = open('.env').readline().strip()

# create prompt template
template = """Question: {input}

Answer: """
llm = OpenAI(model="text-davinci-003")
prompt = PromptTemplate(template=template, input_variables=["input"])
chain = LLMChain(prompt=prompt, llm=llm)

print(chain.run(question))