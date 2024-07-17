
import unittest

from ejercicio_12 import calculate_area


class AreaCalculator(unittest.TestCase):
    
    def test_calculate_square_area(self):
        self.assertEqual(calculate_area(2,2),4)
        self.assertEqual(calculate_area(2,8),16)
    
if __name__=='__main__':
    unittest.main()