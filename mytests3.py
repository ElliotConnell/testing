
#importing unittest module
import unittest
class TestingStringMethods(unittest.TestCase):

	#string equal
	def test_string_equality(self):
		#if both arguments are equal then its a success
		self.assertEqual('ttp' * 5, 'ttpttpttpttpttp')
	#comparing 2 strings 
	def test_string_case(self):
		# if both arguments are equal the its a success
		self.assertEqual('tutorialspoint'.upper(), 'TUTORIALSPOINT')
	# checking whether a string is upper or not
	def test_is_string_upper(self):
		#used to check whether the staement is True of False
		# the result of expression inside the **assertTrue** must be True to pass the test case
		# the result of expression inside the **assertFalse** must be False to pass the test case
		self.assertTrue('TUTORIALSPOINt'.isupper())
		self.assertFalse('TUTORIALSpoint'.isupper())

#running the tests
unittest.main()