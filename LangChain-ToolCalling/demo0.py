from langchain_openai import ChatOpenAI
from langchain.tools import tool
from dotenv import load_dotenv
import os
load_dotenv()
model=ChatOpenAI(
    model='gpt-4.1-mini',
    temperature=0.3,
    api_key=os.getenv('OPENAI_API_KEY')
)
# tool creation
@tool
def calculate_total(
    price:float,
    quantity:int
)->float:
    # Tool documentation & arguments
    # The tool documentation is used by the model to understand what the tool 
    # does and how to use it. The arguments are used to specify the input parameters for the tool.
    '''
    Calculate the total price,
    Args:
    price: price of the item.
    quantity: number of items
    '''
    return price*quantity
# bind the tool with the model
model_with_tools=model.bind_tools([
    calculate_total
])
# step 1- Ask GPT to call the tool
response=model_with_tools.invoke(
    "Calculate the total cost of 5 items at ₹250 each.")
print('Tool Calls')
print(response.tool_calls)

# step 2 -Execute tool
tool_call=response.tool_calls[0] # get the first tool call
# Manually execute the tool with the arguments provided by the model
result=calculate_total.invoke(
    tool_call['args']
)
print(result)


    
