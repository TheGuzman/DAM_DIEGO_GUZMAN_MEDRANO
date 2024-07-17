
import unittest

from ejercicio_8 import imc_calculator


class TestIMCCalculator(unittest.TestCase):
    
    def test_imc(self):
        self.assertAlmostEqual(imc_calculator(68,1.65),24.98)

if __name__=='__main__':
    unittest.main()