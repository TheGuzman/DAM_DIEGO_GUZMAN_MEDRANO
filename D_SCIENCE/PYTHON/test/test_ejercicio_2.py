

import unittest

from ejercicio_2 import calculate_tip



class TestTipCalculator(unittest.TestCase):
    
    def test_positive_check(self):
        self.assertAlmostEqual(calculate_tip(100), 15.0)
        self.assertAlmostEqual(calculate_tip(200), 30.0)
        self.assertAlmostEqual(calculate_tip(50), 7.5)

    def test_zero_check(self):
        with self.assertRaises(ValueError):
            calculate_tip(0)

    def test_negative_check(self):
        with self.assertRaises(ValueError):
            calculate_tip(-50)
            

if __name__ == '__main__':
    unittest.main()