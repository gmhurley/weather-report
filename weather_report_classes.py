import os
import requests

secret_key = os.environ['WUG_Key']
headers = {}


class CurrentConditions:

    """Returns the current conditions at the provided location."""

    def __init__(self, q_string):
        self.q_string = q_string

    def run(self):
        url = 'http://api.wunderground.com/api/{key}/conditions/q/{zip}.json'.format(
                key=secret_key,
                zip=self.q_string
            )

        res = requests.get(url).json()

        location = res['current_observation']['display_location']['full']
        temp = res['current_observation']['temp_f']
        feels_like = res['current_observation']['feelslike_f']
        weather = res['current_observation']['weather']
        time = res['current_observation']['observation_time']
        visibility = res['current_observation']['visibility_mi']
        today_perc = res['current_observation']['precip_today_in']
        wind_speed = res['current_observation']['wind_mph']
        wind_dir = res['current_observation']['wind_dir']

        return location, temp, feels_like, weather, time, visibility, today_perc, wind_speed, wind_dir


class TenDayForcast:

    """Returns the 10 day forcast at the provided location."""

    def __init__(self, q_string):
        self.q_string = q_string

    def run(self):
        url = 'http://api.wunderground.com/api/{key}/forecast10day/q/{zip}.json'.format(
                key=secret_key,
                zip=self.q_string
            )

        ten_day = requests.get(url).json()

        return ten_day['forecast']['txt_forecast']['forecastday']


class SunriseSunset:

    """Returns the sunrise and sunset times at the provided location."""

    def __init__(self, q_string):
        self.q_string = q_string

    def run(self):
        url = 'http://api.wunderground.com/api/{key}/astronomy/q/{zip}.json'.format(
                key=secret_key,
                zip=self.q_string
            )
        sunrise_sunset = requests.get(url).json()

        return sunrise_sunset


class WeatherAlerts:

    """Returns any weather alerts at the provided location."""

    pass


class AllHurricanes:

    """Returns info on any hurricans regardless of location."""

    pass