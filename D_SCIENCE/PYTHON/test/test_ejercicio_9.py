
import unittest

from ejercicio_9 import dollars_to_euros


class TestConversionRate(unittest.TestCase):
    
    def test_dollars_to_euros(self):
        self.assertEqual(dollars_to_euros(1),0.85)
        self.assertEqual(dollars_to_euros(100),85)
        self.assertEqual(dollars_to_euros(0),0)


if __name__=='__main__':
    unittest.main()