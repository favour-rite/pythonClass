import unittest
import float_numbers


class TestCase(unittest.TestCase):

	def test_division_or_square_number_exist(self):
		test_floating_numbers.get_float_numbers(4,5)
	 
	def test_floating_numbers(self):
		
		actual = get_float_number(4,5)
		expected = 0
		self.assertEqual(actual, expected)

		 
		actual = test_floating_numbers.get_float_number(6.2,5.5)
		expected = 2
		self.assertEqual(actual, expected)



	
	def test_that_division_or_square_number_less_than_zero(self):
		self.assertRaises(TypeError,.get_float_number, "-7")

	def test_that__whole_number_raise_exceptation_with_invalid_input(self):
		self.assertRaises(Error,.get_float_number, "34")

	def test_string_input(self):
		self.assertRaises(Error,.get_float_number, "favour")




		