import unittest

from ejercicio_20 import sum_numbers_in_list


class SumNumbersInList(unittest.TestCase):

    def test_sum_in_list(self):
        self.assertEqual(sum_numbers_in_list([1,2,3,4,5,6,7,8,9]), 45 )
        self.assertEqual(sum_numbers_in_list([1,2,3,4,5]), 15 )


