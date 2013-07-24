#tests, will research about python unit tests and will start implenting them.
import unittest
from language import language
from festival import festival
from datetime import date

#Language tests:
#test the greetings logic:
lang = language();
voice = festival();

#any language logic we test here
class language_test(unittest.TestCase):

	#test the greetings builder
	def test_greetings (self):
		#morning check
		self.assertEqual(lang.greet(11), "good morning")
		#afternoon check
		self.assertEqual(lang.greet(13),"good afternoon")
		#night check
		self.assertEqual(lang.greet(20),"good night")

	#test the time format is the same
	def test_time_format (self):
		testday = date(1983, 7, 19)
		self.assertEqual(lang.time(testday),"Tuesday July 19 12:00AM")

#any festival specific tests
class festival_api_test(unittest.TestCase):

	#test the command building
	def test_build_command (self):
		self.assertEqual(voice.build_command("hello world"),"echo hello world | festival --tts")


def main():
	#set up the testing suites:
	language_suite = unittest.TestLoader().loadTestsFromTestCase(language_test)
	festival_suite = unittest.TestLoader().loadTestsFromTestCase(festival_api_test)

	#run each test suite.
	unittest.TextTestRunner(verbosity=2).run(language_suite)
	unittest.TextTestRunner(verbosity=2).run(festival_suite)

if __name__ == '__main__':
    main()