import unittest
import get_odd_even_number


class test_even_and_odd_numbers (unittest.TestCase):

	def  test_even_and_odd_numbers_exist(self):
		number = [1,2,4,5,6]

		test_even_and_odd_numbers.get_odd_sum_even_number(4)


	def test_sum_exist(self):

		actual = get_odd_even_number.get_odd_even_number(4)
		expected = (false,true,true,false,true)

		self.assertEqual(actual, expected)

