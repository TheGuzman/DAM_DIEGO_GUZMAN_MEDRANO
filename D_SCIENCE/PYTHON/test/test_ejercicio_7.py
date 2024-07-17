import unittest

from ejercicio_7 import calculator


class TestCalculator(unittest.TestCase):
    
    def test_sum_calculator(self):
        self.assertEqual(calculator(4,'+', 8),12)
    def test_sum_calculator(self):
        self.assertEqual(calculator(8,'-', 4),4)
    def test_sum_calculator(self):
        self.assertEqual(calculator(4,'*', 8),32)
    def test_sum_calculator(self):
        self.assertEqual(calculator(8,'/', 4),2)



if __name__=='__main__':
    unittest.main()