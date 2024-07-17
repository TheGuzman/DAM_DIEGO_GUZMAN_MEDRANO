
import unittest

from ejercicio_11 import calculate_age


class TestCalculateAge(unittest.TestCase):
    
    def test_calculate_age(self):
        self.assertEqual(calculate_age('31/01/1994'),30)
        self.assertEqual(calculate_age('10/09/1987'),37)
        self.assertEqual(calculate_age('10/09/1982'),42)


if __name__=='__main__':
    unittest.main()