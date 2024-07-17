
import unittest

from ejercicio_16 import odd_even_counter


class OddEvenCounter(unittest.TestCase):

    def test_odd_even_counter(self):
        self.assertEqual(odd_even_counter([2,13,5,48,14]),{'odd':2,'even':3} )
        self.assertEqual(odd_even_counter([0]),{'odd':0,'even':1} )


        