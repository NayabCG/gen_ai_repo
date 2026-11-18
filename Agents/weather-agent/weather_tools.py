import requests
from langchain.tools import tool


@tool
def get_current_weather(city: str) -> str:
    """Get current weather information for a given city."""

    try:

        # Step 1: Get city coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=15
        )

        geo_response.raise_for_status()

        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return f"Location not found: {city}"

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        city_name = location["name"]
        country = location.get("country", "Unknown")

        # Step 2: Call Weather API
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "apparent_temperature,"
                "weather_code,"
                "wind_speed_10m"
            ),
            "timezone": "auto"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=15
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()

        current = weather_data["current"]

        # Step 3: Return weather information
        return f"""
        City: {city_name}
        Country: {country}

        Temperature: {current['temperature_2m']} °C
        Feels Like: {current['apparent_temperature']} °C
        Humidity: {current['relative_humidity_2m']} %
        Wind Speed: {current['wind_speed_10m']} km/h
        Weather Code: {current['weather_code']}
        Observation Time: {current['time']}
        """

    except requests.RequestException as e:

        return f"Weather API request failed: {e}"

    except (KeyError, IndexError, ValueError) as e:

        return f"Unable to process weather information: {e}"