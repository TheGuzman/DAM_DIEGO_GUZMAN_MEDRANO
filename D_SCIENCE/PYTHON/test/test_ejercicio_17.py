
import unittest

from ejercicio_17 import mile_to_kilometer


class MileToKilometerCoverter(unittest.TestCase):

    def test_mile_converter(self):
        self.assertEqual(mile_to_kilometer(100),160.934 )
        self.assertEqual(mile_to_kilometer(250),402.336 )

        