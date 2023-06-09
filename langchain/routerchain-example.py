# Uses a router to determine what type of question it is (generic or math)
# Then uses the appropriate prompt template to answer the question
# Note that the only real difference is the prompt template - they're both using the same LLM

import sys
import os
from langchain.chains.router import MultiPromptChain
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE

if len(sys.argv) < 2:
    print("Please provide the question as a command line argument.")
    sys.exit(1)
question = sys.argv[1]

# read contents of '.env' file
os.environ['OPENAI_API_KEY'] = open('.env').readline().strip()

# create prompt templates
generic_template = """You are a helpful assistant who responds with short answers to questions.
You do not know how to answer any math questions.
When you are asked a math question, you admit that you don't know.

Here is a question:
{input}"""

math_template = """You are a very good mathematician. You are great at answering math questions. \
You are so good because you are able to break down hard problems into their component parts, \
answer the component parts, and then put them together to answer the broader question.
You always prefix your answer with "Ooh, Math! " then a new line.

Here is a question:
{input}"""

prompt_info = [
    {
        "name": "generic", 
        "description": "Good for answering generic questions", 
        "prompt_template": generic_template
    },
    {
        "name": "math", 
        "description": "Good for answering math questions", 
        "prompt_template": math_template
    }
]

llm = OpenAI()

# set up two destination chains with the templates above
destination_chains = {}
for p_info in prompt_info:
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = PromptTemplate(template=prompt_template, input_variables=["input"])
    chain = LLMChain(prompt=prompt, llm=llm)
    destination_chains[name] = chain
default_chain = ConversationChain(llm=llm, output_key="text")

destinations = [f"{p['name']}: {p['description']}" for p in prompt_info]
destinations_str = "\n".join(destinations)
router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(
    destinations=destinations_str
)
router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser(),
)
router_chain = LLMRouterChain.from_llm(llm, router_prompt)

chain = MultiPromptChain(router_chain=router_chain, destination_chains=destination_chains, 
                         default_chain=default_chain, verbose=True)

print(chain.run(question))