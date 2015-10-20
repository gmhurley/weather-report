from weather_report_classes import CurrentConditions

zip_code = input('Please enter a zip code: ')


template = ("The current weather conditions for {location}:\n"
            "Tempature: {temp}" + u"\u00B0" + "F\n"
            "Feels Like: {feels}" + u"\u00B0" + "F\n"
            "Conditions: {cond}\n"
            "Visibility: {vis} miles\n"
            "Percipitation Today: {perc} in.\n"
            "Wind Speed: {wind_speed} mph\n"
            "Wind Direction: {wind_dir}\n"
            "As of:\n"
            "{time}"
            )


cond = CurrentConditions(zip_code).run()

print(template.format(location=cond[0],
                      temp=cond[1],
                      feels=cond[2],
                      cond=cond[3],
                      vis=cond[5],
                      perc=cond[6],
                      wind_speed=cond[7],
                      wind_dir=cond[8],
                      time=cond[4][16:]))
