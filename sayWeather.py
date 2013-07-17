from forecastio import Forecastio
import datetime
from festival import festival

voice = festival();

def main():
    forecast = Forecastio("70f2d5ee3ee858d5869d2038f6001dad")
    result = forecast.load_forecast(40.697488,-73.979681,
                                   time=datetime.datetime.now(), units="us")
    #print result


    if result['success'] is True:

        voice.say("good morning humans")

        # print "===========Hourly Data========="
        by_hour = forecast.get_hourly()
        print "Hourly Summary: %s" % (by_hour.summary)
        voice.say("Hourly Summary.")
        voice.say(by_hour.summary)

        # for hourly_data_point in by_hour.data:
        #     print hourly_data_point

        # print "===========Daily Data========="
        by_day = forecast.get_daily()
        print "Daily Summary: %s" % (by_day.summary)
        voice.say("Daily Summary")
        voice.say(by_day.summary)

        for daily_data_point in by_day.data:
            print daily_data_point
            #engine.say(daily_data_point)
    else:
        print "A problem occurred communicating with the Forecast.io API"


if __name__ == "__main__":
    main()
