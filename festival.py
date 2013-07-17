#Dead simple festival "api"
import os

class festival():

	#you will need festival installed on the machine.
	def say(self,text):
		os.system("echo " + str(text) + " | festival --tts")
