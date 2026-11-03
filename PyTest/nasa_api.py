from datetime import date, datetime
import requests

from weather import WeatherDay

class NasaPS:
    BASE_URL = (
        "https://power.larc.nasa.gov/api/temporal/daily/point" 
    )



    def __init__(self, latitude: float, longitude: float, elevation: float ):
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation

    def get_daily_weather(self, 
                          start_date=20240101,
                          end_date= 20240115 
     ) -> list[WeatherDay]:
        params = {
            "parameters": "T2M,PRECTOTCORR",
            "community": "AG",
            "latitude": self.latitude,
            "longitude": self.longitude,
            "start": start_date,
            "end": end_date,
            "format": "JSON",
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=100
        )

        response.raise_for_status()
        data = response.json()

        parameters = data["properties"]["parameter"]

        temperatures = parameters["T2M"]
        precipitations = parameters["PRECTOTCORR"]

        weather_records = []

        for date_string in sorted(temperatures):
            temp = temperatures[date_string]
            rain = precipitations.get(date_string)

            if temp == -999:
                temp = None
            if rain == -999:
                rain = None
            real_date = datetime.strptime(date_string, "%Y%m%d").date()

            weather_day = WeatherDay(
                date=real_date,
                temperature=temp,
                precipitation=rain
            )
            weather_records.append(weather_day)

        return weather_records