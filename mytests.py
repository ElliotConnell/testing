import unittest

class MyFirstTests(unittest.Testcase):
	def test_hello(self):
		self.assertEqual(hello_world(), 'hello world')