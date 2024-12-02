import unittest
import get_sum_of_even_numbers


class Test_sum(unittest.TestCase):

	def test_sum_exist(self):
		test_sum.get_sum_of_even_numbers(5)

	def test_sum_exist(self):
		actual = test_sum.get_sum_of_even_numbers(1,2,3,4,5)
		expected = 6
		self.assertEqual(actual, expected)








if __name__ == "__main__":
	unittest.main()
