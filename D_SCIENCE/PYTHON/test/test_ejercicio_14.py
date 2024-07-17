

import unittest

from ejercicio_14 import calculate_discount


class DiscoutCalculator(unittest.TestCase):
    
    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(100),80)
        self.assertEqual(calculate_discount(150),120)
    
if __name__=='__main__':
    unittest.main()