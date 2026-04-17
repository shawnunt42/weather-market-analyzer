import requests
from datetime import datetime, timedelta

def get_lat_lon(city, state):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "city": city,
        "state": state,
        "country": "USA",
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "weather-market-edge-analyzer"
    }

    res = requests.get(url, params=params, headers=headers)
    data = res.json()

    if not data:
        return None, None

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    return lat, lon


def get_hourly_forecast(lat, lon):
    headers = {
        "User-Agent": "weather-market-edge-analyzer",
        "Accept": "application/geo+json"
    }

    points_url = f"https://api.weather.gov/points/{lat},{lon}"
    res = requests.get(points_url, headers=headers)
    data = res.json()

    forecast_url = data["properties"]["forecastHourly"]

    res = requests.get(forecast_url, headers=headers)
    forecast = res.json()

    return forecast["properties"]["periods"]


def get_high_low_for_date(periods, target_date):
    temps = []

    for p in periods:
        start_time = p["startTime"]

        if start_time.endswith("Z"):
            dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        else:
            dt = datetime.fromisoformat(start_time)

        if dt.date() == target_date:
            temps.append(p["temperature"])

    if not temps:
        return None, None

    return max(temps), min(temps)


def get_target_date(choice, custom_date_str=None):
    today = datetime.now().date()

    if choice == "1":
        return today
    elif choice == "2":
        return today + timedelta(days=1)
    elif choice == "3":
        return datetime.strptime(custom_date_str, "%Y-%m-%d").date()
    else:
        return None