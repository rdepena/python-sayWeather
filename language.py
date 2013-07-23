#this file is responsible for all the language tweaks
#or a collection of pre-determined sentances
class language ():

	#I expect to be passed a 24 hour format hour int from 0 to 24
	def greet(self, hour) :
		#start the sentace with
		greeting = "good "

		if (hour < 13) :
			greeting = greeting + "morning"
		elif (hour < 19) :
			greeting = greeting + "afternoon"
		else :
			greeting = greeting + "night"
		return greeting;

	# perhaps a dateTime is in order...
	def time(self, datetime) :

		return datetime.strftime("%A %B %d %I:%M%p")
