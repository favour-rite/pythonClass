import unittest
import my_discount


class TestCase(unittest.TestCase):

	def test_my_discount_exist(self):
		test_my_discount.get_my_d()
	 
	def test_division_or_square_number(self):
		
		actual = get_my_discount(15)
		expected = 127.5
		self.assertEqual(actual, expected)

		 
			
	def test_that_division_or_square_number_less_than_zero(self):
		self.assertRaises(TypeError,.get_my_discount, "-7")

	def test_that_my_discount_exceptation_with_decimal_input(self):
		self.assertRaises(Error,.get_my_discount, "3.4")

	def test_string_input(self):
		self.assertRaises(Error,.get_my_discount, "favour")




		