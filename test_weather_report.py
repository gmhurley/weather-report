import os
import requests_mock
from weather_report_classes import CurrentConditions, TenDayForcast, SunriseSunset, WeatherAlerts, AllHurricanes

secret_key = os.environ['WUG_Key']


@requests_mock.Mocker()
def test_current_conditions(m):
    with open('test_current_cond.json') as current_cond:
        m.get('http://api.wunderground.com/api/{}/conditions/q/27104.json'.format(secret_key), text=current_cond.read())

    current_conditions = CurrentConditions('27104')
    res = current_conditions.run()

    assert res == ('Winston Salem, NC', 43.5, '44', 'Clear',
                   'Last Updated on October 19, 9:15 PM EDT', '10.0', '0.00', 0.0, 'SE')
