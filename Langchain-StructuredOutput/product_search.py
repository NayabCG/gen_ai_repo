from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0.3,
    api_key=os.getenv("OPENAI_API_KEY")
)
class ProductSearch(BaseModel):

    category: str = Field(
        description="Product category"
    )

    max_price: int = Field(
        description="Maximum budget"
    )

    ram: str = Field(
        description="Required RAM"
    )

    storage: str = Field(
        description="Required storage"
    )
structured_model = model.with_structured_output(ProductSearch)

user_input = input("Enter your product requirements: ")

response = structured_model.invoke(user_input)

print(response)