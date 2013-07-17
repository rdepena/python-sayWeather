#Dead simple festival "api" lol.
import os

class festival():

	#you will need festival installed on the machine.
	def say(self,text):
		os.system("echo " + str(text) + " | festival --tts")
