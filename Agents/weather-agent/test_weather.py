import requests

url = "https://geocoding-api.open-meteo.com/v1/search"

# Parameters for the API request
params = {
    "name": "Hyderabad",
    "count": 1,
    "language": "en",
    "format": "json"
}
# Make the API request
response = requests.get(
    url,
    params=params,
    timeout=15
)
# Check if the request was successful
if response.status_code == 200:
    data = response.json() # Parse the JSON response
    print(data)