

import unittest

from ejercicio_13 import is_prime_number


class IsPrimeNumber(unittest.TestCase):
    
    def test_check_if_prime_number(self):
        self.assertFalse(is_prime_number(407))
        self.assertFalse(is_prime_number(100))
        self.assertFalse(is_prime_number(1))
        self.assertTrue(is_prime_number(3),True)
        self.assertTrue(is_prime_number(7),True)

    
if __name__=='__main__':
    unittest.main()