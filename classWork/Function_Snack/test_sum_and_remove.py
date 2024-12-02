import unittest

import get_sum_and_remove



class test_remove_sum_number(unittest.TestCase):
	def test_remove_sum_number(self):

		number = [1,2,3]


		actual = get_sum_and_remove.get_sum_and_remove(number)
		expected = 12

		self.assertEqual(actual,expected)