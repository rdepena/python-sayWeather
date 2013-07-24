#Dead simple festival "api" lol.
import os

class festival():

	#you will need festival installed on the machine.
	def say(self,text):
		os.system(self.build_command(text))

	def build_command(self, text):
		return "echo %s | festival --tts" %(text)