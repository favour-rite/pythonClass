import unittest

import get_missing_number

class test_missing_number(unittest.TestCase):
	def test_missing_number_exist(self):
		actual = get_missing_number.get_missing_number(number.len)
		expected = 0 
		self.assertEqual(actual)