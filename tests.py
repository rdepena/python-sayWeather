#tests, will research about python unit tests and will start implenting them.
import unittest
from language import language
from festival import festival
from datetime import date

#Language tests:
#test the greetings logic:
lang = language();

class languageTest(unittest.TestCase) :

	def testGreetings(self):
		#morning check
		self.failUnless(lang.greet(11) == "good morning")
		#afternoon check
		self.failUnless(lang.greet(13) == "good afternoon")
		#night check
		self.failUnless(lang.greet(20) == "good night")

	def testTime(self):
		testday = date(1983, 7, 19)
		self.failUnless(lang.time(testday) == "Tuesday July 19 12:00AM")

def main():
	unittest.main();

if __name__ == '__main__':
    main()


