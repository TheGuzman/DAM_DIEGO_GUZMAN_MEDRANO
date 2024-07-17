
import unittest

from ejercicio_18 import word_counter


class WordCounter(unittest.TestCase):

    def test_word_converter(self):
        self.assertEqual(word_counter('This is a test'),4 )
        self.assertEqual(word_counter(''), 0)
        self.assertEqual(word_counter('Words dog cat parror computer'), 5)
