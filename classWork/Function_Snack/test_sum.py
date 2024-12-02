import unittest
import get_sum_of_even_numbers


class test_sum(unittest.TestCase):



	def test_that_get_sum_of_even_numbers_returns(self):
		list = [1,2,3,4,5]
		actual = get_sum_of_even_numbers.get_sum_of_even_numbers(list)
		expected = 6
		self.assertEqual(actual, expected)
	








if __name__ == "__main__":
	unittest.main()
