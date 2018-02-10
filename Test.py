import unittest
import Mymath

class Test(unittest.TestCase):

	def setUp(self):
		pass
	
	def test_addition(self):
		self.assertEqual(Mymath.addition(11,2),13)

	def test_subtraction(self):
		self.assertEqual(Mymath.subtraction(5,1),4)

	def test_multiplication(self):
		self.assertEqual(Mymath.multiplication(4,5),20)
	
	def test_division(self):
		self.assertEqual(Mymath.division(12,2),6)
	
	def test_divisionbyzero(self):
		with self.assertRaises(ZeroDivisionError):Mymath.division(7,0)

if __name__ == '__main__':
	unittest.main()