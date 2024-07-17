import unittest

from ejercicio_19 import is_leap_year


class IsLeapYear(unittest.TestCase):

    def test_leap_year(self):
        self.assertEqual(is_leap_year(2024), True )
        self.assertEqual(is_leap_year(2020), True )
        self.assertEqual(is_leap_year(2023), False )
        self.assertEqual(is_leap_year(0), True )


