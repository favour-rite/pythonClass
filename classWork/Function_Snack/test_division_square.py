import unittest
import remainder_or_squaroot


class TestCase(unittest.TestCase):

	def test_division_or_square_number_exist(self):
		test_division_or_square.get_remainder_or_squareroot(5)
	 
	def test_division_or_square_number(self):
		
		actual = get_remainder_or_squareroot(5,5)
		expected = 25
		self.assertEqual(actual, expected)

		 
		actual = test_division_or_square_number.get_remainder_or_squareroot(6)
		expected = 36
		self.assertEqual(actual, expected)



	
	def test_that_division_or_square_number_less_than_zero(self):
		self.assertRaises(TypeError,division_or_square_number.get_remainder_or_squareroot, "-7")

	def test_that_division_or_square_raise_exceptation_with_invalid_input(self):
		self.assertRaises(Error,division_or_square_number.get_remainder_or_squareroot, "3.4")

	def test_string_input(self):
		self.assertRaises(Error, division_or_square_number.get_remainder_or_squareroot, "favour")




		