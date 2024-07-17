import unittest

from ejercicio_6 import palindrome_checker


class TestPalindrome(unittest.TestCase):
    
    def test_palindrome_even_word(self):
        self.assertTrue(palindrome_checker('anna'))
        self.assertFalse(palindrome_checker('mama'))
        self.assertTrue(palindrome_checker('elle'))

    def test_palindrome_odd_word(self):
        self.assertTrue(palindrome_checker('repaper'))
        self.assertTrue(palindrome_checker('kayak'))

    def test_palindrome_capitalized_word(self):
        self.assertTrue(palindrome_checker('RePapeR'))
        self.assertTrue(palindrome_checker('KaYak'))

    def test_palindrome_sentence(self):
        self.assertTrue(palindrome_checker('Never odd or even'))



if __name__=='__main__':
    unittest.main()