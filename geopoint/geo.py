from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform
from folium import Marker

class Geopoint(Marker):

    latitude_range = (-74.11, 74.11)
    longiture_range = (-18.64, 18.64)

    def __init__(self, longitude, latitude):
        super().__init__(location =[latitude, longitude])
        self.longitude = longitude
        self.latitude = latitude

    def closest_parallel(self):
        return round(self.longitude)

    def get_city(self):
        zf = TimezoneFinder()
        return zf.timezone_at(lng=self.longitude, lat=self.latitude)

    def get_time(self):
        return datetime.now(timezone(self.get_city()))

    def get_weather(self):
        weather = Weather(apikey="6b1bc321cb07b1ef9b875a79248a6484", \
                          lon=self.longitude, lat=self.latitude)
        return weather.next_12h_simplified()

    @classmethod
    def random(cls):
        return cls(latitude = uniform(-74.11, 74.11), longitude = uniform(-18.64, 18.64))

