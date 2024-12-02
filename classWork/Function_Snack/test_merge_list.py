import unittest
import get_merge_list


class test_merge_list(unittest.TestCase):



	def test_merge_list(self):
		array1 = [3,4,9,10] 
		array2 = [1,5,7,8]


		actual = get_merge_list.get_merge_list(array1, array2)
		
		expected = [1,3,4,5,7,8,9,10]
		self.assertEqual(actual, expected)


