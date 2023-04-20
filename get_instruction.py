import openai
import os

prompt = """ Context: You are a software assistant. you will answer the users questions step by step. 
giving clear instruction in json form on what to click on and if necessary what code to enter and where. 

Here are two examples:
User: How do I sum up a column of numbers in google sheets?
response: [{action:"message", message: "first click on the cell where you want the sum result to appear"},{action:"add_code", code: "=sum("},{action:"message", message: "sum only requires one input, the cells that need to be summed up"}, {action:"message", message: "select the cells you want to sum"}, {action:"message", message: "no more cells inputs are required"},{action:"message", message: "now hit return"}]
User: How do I sum up a column of numbers in google sheets?

User: How do I change the colours of a cell based on the numerical values?
response:[{action:"message", message: "This requires conditional formatting"},{action:"move mouse to", target: "Format"},{action:"click mouse", button: "left"}, {action:"move mouse to", target: "Conditional formatting"},{action:"click mouse", button: "left"}, {action:"move mouse to", target: "Apply_to_range"},{action:"message", message: "Select the cells you want to be formatted"}, {action:"message", message: "when finished click done"}]

User: How do I rank numbers?
"""

prompt = """ Context: You are a software assistant. you will answer the users questions step by step. 
giving clear instruction in json form on what to click on and if necessary what code to enter and where. 

User: How do I change the colours of a cell based on the numerical values?

response: click Format, click conditional formatting, Edit format rules, click Done 

User: How do I center text?
"""


# Set up OpenAI API credentials
print(os.environ["OPENAI_API_KEY"])
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up OpenAI API request parameters
model_engine = "text-davinci-002"
temperature = 0.5
max_tokens = 1024

# Make request to OpenAI API
print("hitting open ai")
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=temperature,
    )
#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
print(response)