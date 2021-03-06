from forecastio import Forecastio
from datetime import datetime
from festival import festival
from language import language

voice = festival();
lang = language();

def main():
    forecast = Forecastio("")
    time=datetime.now()
    units = "us"
    result = forecast.load_forecast(40.697488,-73.979681,time, units)

    if result['success'] is True:

        #say the greeting:
        voice.say(lang.greet(time.hour))

        #say the time.
        voice.say(lang.time(time))

        # print "===========Hourly Data========="
        by_hour = forecast.get_hourly()
        print "Hourly Summary: %s" % (by_hour.summary)
        voice.say(lang.summary_description())
        voice.say(by_hour.summary)

    else:
        print "A problem occurred communicating with the Forecast.io API"


if __name__ == "__main__":
    main()
