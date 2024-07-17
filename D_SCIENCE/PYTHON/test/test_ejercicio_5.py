

import unittest

from ejercicio_5 import calculate_sum_even_numbers


class TestEvenCounter(unittest.TestCase):
    
    def test_even_number_counter(self):
        self.assertEqual(calculate_sum_even_numbers(100), 2550)



if __name__=='__main__':
    unittest.main()