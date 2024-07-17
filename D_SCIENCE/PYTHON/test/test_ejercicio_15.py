
import unittest

from ejercicio_15 import time_converter


class TestTimeConverter(unittest.TestCase):

    def test_time_converter(self):
        self.assertAlmostEqual(time_converter(145), '145 are 2 hours and 25 minutes')
        self.assertAlmostEqual(time_converter(345), '345 are 5 hours and 45 minutes')
        self.assertAlmostEqual(time_converter(500), '500 are 8 hours and 20 minutes')