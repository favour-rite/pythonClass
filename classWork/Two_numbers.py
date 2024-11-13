import unittest

import two_numbers

class TestCase(unittest.TestCase):
		
	def test_two_numbers_exists(self):
		two_numbers.get_two_number(2)

		
	def test_two_numbers(digit):
		actual = two_numbers.get_two_number(2)
		expected = 4
		self.assertEqual(actual, expected)   
	