
import unittest

from ejercicio_3 import check_user_is_adult

class TestAdultChecker(unittest.TestCase):

    def test_positive_age_adult_checker(self):
        self.assertTrue(check_user_is_adult(18))
        self.assertFalse(check_user_is_adult(5))

    def test_negative_age_checker(self):
        with self.assertRaises(ValueError):
            check_user_is_adult(-5)

    def test_wrong_inpyt_type_age_checker(self):
        with self.assertRaises(TypeError):
            check_user_is_adult('5')

if __name__ == '__main__':
    unittest.main()