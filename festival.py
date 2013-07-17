#Dead simple festival "api"
import os

class festival():

	
	def say(self,text):
		os.system("echo " + str(text) + " | festival --tts")
