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


@requests_mock.Mocker()
def test_ten_day(m):
    with open('test_10_day.json') as ten_day:
        m.get('http://api.wunderground.com/api/{}/forecast10day/q/27104.json'.format(secret_key), text=ten_day.read())

    ten_day_forecast = TenDayForcast('27104')
    res = ten_day_forecast.run()

    print(res)

    assert res[0]['title'] == 'Tuesday'
    assert res[19]['fcttext'] == 'Partly cloudy skies early followed by mostly cloudy skies and a few showers later at night. Low 39F. Winds light and variable. Chance of rain 30%.'


@requests_mock.Mocker()
def test_sunrise_sunset(m):
    with open('sunrise_sunset.json') as sunrise_sunset:
        m.get('http://api.wunderground.com/api/{}/astronomy/q/27104.json'.format(secret_key), text=sunrise_sunset.read())

    sunrise_sunset_times = SunriseSunset('27104')
    res = sunrise_sunset_times.run()

    print(res)

    assert res['sun_phase']['sunrise']['hour'] == "7"
    assert res['sun_phase']['sunrise']['minute'] == "32"
    assert res['sun_phase']['sunset']['hour'] == "18"
    assert res['sun_phase']['sunset']['minute'] == "39"


@requests_mock.Mocker()
def test_heat_alert(m):
    with open('alert_heat.json') as heat_alert:
        m.get('http://api.wunderground.com/api/{}/alerts/q/50301.json'.format(secret_key), text=heat_alert.read())

    alerts = WeatherAlerts('50301')
    res = alerts.run()

    assert res[:12] == '11:14 am CDT'
    assert res[48:61] == 'Heat advisory'
    assert res[-6:-3:] == 'Mjb'


@requests_mock.Mocker()
def test_empty_alert(m):
    with open('alert_blank.json') as empty_alert:
        m.get('http://api.wunderground.com/api/{}/alerts/q/27104.json'.format(secret_key), text=empty_alert.read())

    alerts = WeatherAlerts('27104')
    res = alerts.run()

    print(res)

    assert res == 'Whew! No local alerts.'


@requests_mock.Mocker()
def test_hurricane(m):
    with open('hurricane.json') as hurricane:
        m.get('http://api.wunderground.com/api/{}/currenthurricane/view.json'.format(secret_key), text=hurricane.read())

    hurricanes = AllHurricanes
    res = hurricanes.run()

    assert res[:20] == 'Name: Hurricane Olaf'
