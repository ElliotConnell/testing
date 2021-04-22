# importing unittest module
import unittest

class TestingStrengMethods(unittest.TestCase):
	# string equal
	def test_string_equality(self):
		# if both arguments are equal then it's success
		self.assertEqual('ttp' * 5, 'ttpttpttpttpttp')

	#comparing the two strings
	def test_string_case(self):
		#if both arguments are equal then it's a success
		self.assertEqual('tutorialspoint'.upper(), 'TUTORIALSPOINT')

	#checking if the string is upper or not
	def test_string_is_upper(self):
		# used to check whether the statement is True or False
		# the result of expression inside the **asserttrue** must be True to pass the test case
		# the result of expression inside the **assertfalse** must be False to pass the test case
		self.assertTrue('TUTORIALSPOINT'.isupper())
		self.assertFalse('TUTORIALSpoint'.isupper())
#running the tests
unittest.main()

