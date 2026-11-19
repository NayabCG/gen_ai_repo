import requests

from dotenv import load_dotenv
from langchain.tools import tool

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from database import get_employee


load_dotenv()


# =====================================
# 1. HR RAG TOOL
# =====================================

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store = FAISS.load_local(
    "vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)


@tool
def search_company_documents(question: str) -> str:
    """Search HR and company policy documents for relevant information."""

    results = vector_store.similarity_search(
        question,
        k=4
    )

    if not results:
        return "No relevant information found."

    context = []

    for doc in results:

        source = doc.metadata.get(
            "source", "Unknown"
        )

        context.append(
            f"Source: {source}\n"
            f"Content: {doc.page_content}"
        )

    return "\n\n".join(context)


# =====================================
# 2. FINANCE DATABASE TOOL
# =====================================

@tool
def get_employee_financial_details(
    employee_id: str
) -> str:
    """Retrieve employee department and salary information using employee ID."""

    employee = get_employee(employee_id)

    if not employee:

        return "Employee not found."

    return (
        f"Employee ID: {employee[0]}\n"
        f"Name: {employee[1]}\n"
        f"Department: {employee[2]}\n"
        f"Monthly Salary: Rs. {employee[3]}"
    )


# =====================================
# 3. IT SUPPORT TOOL
# =====================================

@tool
def get_it_support_information(issue: str) -> str:
    """Provide company IT support guidance for password, account and laptop issues."""

    issue = issue.lower()

    if "password" in issue:

        return """
        Password Reset Instructions:

        1. Open company login portal.
        2. Select Forgot Password.
        3. Verify your identity.
        4. Create a new password.
        """

    elif "locked" in issue or "account" in issue:

        return """
        Account Support:

        Contact the IT helpdesk.
        Verify your employee identity.
        Request account unlock assistance.
        """

    elif "laptop" in issue:

        return """
        Laptop Support:

        Raise a ticket through the IT support portal.
        Describe the hardware or software issue.
        """

    else:

        return """
        Please contact the IT helpdesk
        for further assistance.
        """


# =====================================
# 4. EXTERNAL WEATHER API TOOL
# =====================================

@tool
def get_weather(city: str) -> str:
    """Retrieve current weather information for a city using Open-Meteo."""

    try:

        geo_response = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json"
            },
            timeout=15
        )

        geo_response.raise_for_status()

        geo_data = geo_response.json()

        if not geo_data.get("results"):

            return "City not found."

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        weather_response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "wind_speed_10m"
                ),
                "timezone": "auto"
            },
            timeout=15
        )

        weather_response.raise_for_status()

        weather = weather_response.json()["current"]

        return (
            f"City: {location['name']}\n"
            f"Country: {location.get('country', 'Unknown')}\n"
            f"Temperature: {weather['temperature_2m']} Celsius\n"
            f"Humidity: {weather['relative_humidity_2m']}%\n"
            f"Wind Speed: {weather['wind_speed_10m']} km/h"
        )

    except requests.RequestException as e:

        return f"Weather service unavailable: {e}"