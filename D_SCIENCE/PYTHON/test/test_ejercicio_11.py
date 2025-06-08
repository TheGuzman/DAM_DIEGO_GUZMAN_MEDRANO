
import unittest

from ejercicio_11 import calculate_age


class TestCalculateAge(unittest.TestCase):
    
    def test_calculate_age(self):
        self.assertEqual(calculate_age('31/01/1994'),31)
        self.assertEqual(calculate_age('10/09/1987'),38)
        self.assertEqual(calculate_age('10/09/1982'),43)


if __name__=='__main__':
    unittest.main()