import unittest 
import functionpratice

class TestCubeFunction(unittest) : 
	def test_that_cube_function_exists(self):
		functionpratise.get_cube(3)

	def test_that_cube_function_returns_correct_value(self):
		actual = functionpratice.get_cube(3)
		expected = 27
		self.assertEqual(actual,expected)
		actual = functionpractice.get_cube(10)
		expected = 1000
		self.assertEqual(actual,expected)

	def test_that_function_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, functionpratice.get_cube, "moses")
		
	def test_that_cube_function_retuns_correct_value_with_float(self):
		actual = functionpratice.get_cube(2.3)
		expected = 12.167
		slef.assertEqual(actual, expected)