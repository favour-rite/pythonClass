import unittest

import multiply

class TestMultiply(unittest.TestCase):
		
	def test_two_numbers_exists(self):
		multiply.get_two_number(2)

		
	def test_two_numbers(self):
		actual = multiply.get_two_number(2)
		expected = 4
		self.assertEqual(actual, expected)   

