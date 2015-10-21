from weather_report_classes import CurrentConditions, TenDayForcast, SunriseSunset, WeatherAlerts, AllHurricanes

def get_weather(zip_code):
    template = ("\nThe current weather conditions for {location}:\n\n"
                "Tempature: {temp}" + u"\u00B0" + "F\n"
                "Feels Like: {feels}" + u"\u00B0" + "F\n"
                "Conditions: {cond}\n"
                "Visibility: {vis} miles\n"
                "Percipitation Today: {perc} in.\n"
                "Wind Speed: {wind_speed} mph\n"
                "Wind Direction: {wind_dir}\n"
                "As of:\n"
                "{time}\n\n"
                "10 Day forecast:\n\n"
                "{ten_day}\n\n"
                "Sunrise/Sunset Times:\n"
                "Sunrise: {sunrise}\n"
                "Sunset: {sunset}\n\n"
                "Weather Alerts:\n"
                "{alerts}\n\n"
                "Hurricanes World Wide:\n"
                "{hurricanes}"
                ""
                )

    cond = CurrentConditions(zip_code).run()

    ten_day = TenDayForcast(zip_code).run()
    ten_day_lst = [x['title'] + ': ' + x['fcttext'] for x in ten_day]
    ten_day_str = '\n\n'.join(ten_day_lst)

    sun = SunriseSunset(zip_code).run()
    sunrise = sun['sun_phase']['sunrise']['hour'] + ":" + sun['sun_phase']['sunrise']['minute']
    sunset = sun['sun_phase']['sunset']['hour'] + ":" + sun['sun_phase']['sunset']['minute']

    alerts = WeatherAlerts(zip_code).run()

    hurricanes = AllHurricanes.run()

    print(template.format(location=cond[0],
                          temp=cond[1],
                          feels=cond[2],
                          cond=cond[3],
                          vis=cond[5],
                          perc=cond[6],
                          wind_speed=cond[7],
                          wind_dir=cond[8],
                          time=cond[4][16:],
                          ten_day=ten_day_str,
                          sunrise=sunrise,
                          sunset=sunset,
                          alerts=alerts,
                          hurricanes=hurricanes))


while True:
    zip_code = input('Please enter a zip code (or CTRL + C to quit): ')
    get_weather(zip_code)
