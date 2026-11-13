
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Step 1: Load environment variables
load_dotenv()

# Step 2: Initialize GPT-5.5 model
model = ChatOpenAI(
    model="gpt-5.5",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Step 3: Create reusable prompt template
prompt_template = ChatPromptTemplate.from_messages([

    (
        "system",
        """
        You are an enterprise eCommerce customer support assistant.

        Your responsibilities:
        1. Answer customer queries professionally.
        2. Use only the information provided.
        3. Never invent order status or delivery information.
        4. If information is missing, clearly mention it.
        5. Explain refund and cancellation procedures.
        6. Keep responses simple and concise.

        Response format:
        - Greeting
        - Answer to customer query
        - Recommended next action
        """
    ),

    (
        "human",
        """
        Customer Details:
        Name: {customer_name}
        Customer ID: {customer_id}

        Order Details:
        Order ID: {order_id}
        Product: {product_name}
        Order Status: {order_status}
        Delivery Date: {delivery_date}

        Customer Query:
        {customer_query}
        """
    )
])

# Step 4: Prepare dynamic customer information
customer_data = {
    "customer_name": "Santhosh",
    "customer_id": "CUST1001",
    "order_id": "ORD1001",
    "product_name": "HP Laptop",
    "order_status": "Shipped",
    "delivery_date": "15 November 2026",
    "customer_query": "Where is my order?"
}

# Step 5: Format the prompt using dynamic data
formatted_prompt = prompt_template.invoke(customer_data)

# Step 6: Send formatted prompt directly to GPT-5.5
response = model.invoke(formatted_prompt)

# Step 7: Display AI response
print("\nCustomer Support Response:")
print(response.content)
