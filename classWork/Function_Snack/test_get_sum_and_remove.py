import unittest

import get_sum_and_remove



class test_remove_sum_number(unittest.TestCase):
	def test_remove_sum_number(self):

		number = [1,2,3,4,5]
		

		actual = get_sum_and_remove.get_sum_and_remove(self)
		expected = 60
		self.assertEqual(actual,expected)