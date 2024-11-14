import unittest

import get_sum

class test_list_and_sum_of_numbers(unittest.TestCase):

	def test_list_and_sum_of_numbers_exist(self):
		number = [4,8,6,3,2]
		test_list_and_sum_of_numbers.get_sum(numbers)
		expected = 0
		actual = 17
		assertEqual()