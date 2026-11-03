from urllib import response

import requests
from nasa_api import NasaPS

def format_value (value , unit):
    if value is None:
        return "N/A"
    else:
        return f"{value:.2f} {unit}"

try: 
    service = NasaPS(latitude=13.62, longitude=123.18, elevation=56.54)
    days = service.get_daily_weather()
    rainy_days = [day for day in days if day.is_rainy()]
    for day in days:
        temp = format_value(day.temperature, "°C")
        rain = format_value(day.precipitation, "mm")

        print(f"Date: {day.date}, Temperature: {temp}, Precipitation: {rain}, Rainy?: {day.is_rainy()}")
    
    print(f"\n Total Records: {len(days)}")
    print(f"Rainy Days: {len(rainy_days)}, Date: {', '.join(str(day.date) for day in rainy_days)}")

except (
    requests.exceptions.RequestException,
    KeyError,
    ValueError,
    TypeError
) as error:
    print("Error bai:", error)