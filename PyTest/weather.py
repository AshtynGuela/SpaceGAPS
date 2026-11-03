from dataclasses import dataclass
from datetime import date

@dataclass 
class WeatherDay:
    date: date
    temperature: float | None
    precipitation: float | None
    def is_rainy(self) -> bool:
        return self.precipitation is not None and self.precipitation > 1

