import unittest
import sys
from test_base import run_unittests
import word_processor


class MyTestCase(unittest.TestCase):

    def test_convert_to_word_list(self):
        text = "Hello. Mah nems jeiff. How may I help you?"
        words = word_processor.convert_to_word_list(text)
        self.assertEqual(words, ["hello", "mah", "nems", "jeiff", "how", "may", "i", "help", "you"])

    def test_words_longer_than(self):
        text = "Hi how are you, Ed ?"
        words = word_processor.words_longer_than(2, text)
        self.assertEqual(words, ["how", "are", "you"])

    def test_words_lengths_map(self):
        text = "Adam said to Eve, cover yourself with leafs"
        test_dict = word_processor.words_lengths_map(text)
        self.assertEqual(test_dict, {2: 1, 3: 1, 4: 3, 5: 2, 8: 1})

    def test_letters_count_map(self):
        text = "Adam said to Eve, cover yourself with leafs"
        test_dict = word_processor.letters_count_map(text)
        self.assertEqual(test_dict, {'a': 4, 'b': 0, 'c': 1, 'd': 2, 'e': 5, 'f': 2, 'g': 0, 'h': 1,
        'i': 2, 'j': 0, 'k': 0, 'l': 2, 'm': 1, 'n': 0, 'o': 3, 'p': 0, 'q': 0, 'r': 2, 's': 3, 't': 2,
        'u': 1, 'v': 2, 'w': 1, 'x': 0, 'y': 1, 'z': 0})

    def test_most_used_character(self):
        text = "Adam said to Eve, cover yourself with leafs"
        test_dict = word_processor.most_used_character(text)
        self.assertEqual(test_dict, "e")