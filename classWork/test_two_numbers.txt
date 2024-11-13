
from unittest import TestCase

import Two_numbers

class TestTwoNumbers(TestCase):
	
	def test_two_numbers_exists(self):
		two_numbers.get_number(2)

		
	def test_two_numbers(digit):
		actual = two_numbers.get_number(2)
		expected = 4
		self.assertEqual(actual, expected)   
	