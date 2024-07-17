import unittest

from ejercicio_4 import vowel_counter

class CheckVowelCounter(unittest.TestCase):

    def test_check_vowels_in_word(self):
        self.assertEqual(vowel_counter('hello'), 2)
        self.assertEqual(vowel_counter('eooo'), 4)
        self.assertEqual(vowel_counter('trx'), 0)

        
if __name__ == '__main__':
    unittest.main()