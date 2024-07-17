import unittest

from ejercicio_1 import transform_celsius_to_farenheit


class TestCelsiusToFarenheit(unittest.TestCase):

    def test_positive_celsius(self):
        self.assertEqual(transform_celsius_to_farenheit(32), 89.6, "Should be 89.6 ")

    def test_cero_celsius(self):
        self.assertEqual(transform_celsius_to_farenheit(0), 32, "Should be 32 ")

    def test_negative_celsius(self):
        self.assertEqual(transform_celsius_to_farenheit(-5), 23, "Should be 23")

    def test_negative_farenheit(self):
        self.assertEqual(transform_celsius_to_farenheit(-100),-148, "Should be -148")

if __name__ == '__main__':
    unittest.main()