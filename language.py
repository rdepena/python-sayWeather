#this file is responsible for all the language tweaks
#or a collection of pre-determined sentances
class language ():

	#I expect to be passed a 24 hour format hour int from 0 to 24
	def greet(self, hour) :
		#start the sentace with
		pre = "good"
		suffix = ""
		if (hour < 13) :
			suffix = "morning"
		elif (hour < 19) :
			suffix = "afternoon"
		else :
			suffix = "evening"
		return "%s %s"%(pre, suffix);

	# perhaps a dateTime is in order...
	def time(self, datetime):
		return datetime.strftime("%A %B %d %I:%M%p")

	def summary_description(self):
		return "The weather expected today is"
