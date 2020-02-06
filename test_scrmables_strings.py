import unittest
from scrmabled_strings import *
import os

src_dir = os.getcwd()
search_file = '{}/files/search_string'.format(src_dir, )


class MyTestCase(unittest.TestCase):
    def test_limitation_1(self):
        dict_filename = '{}/files/dictionary_words_limitation_1'.format(src_dir, )
        response = print_scramble_word_count(dict_filename, search_file)
        self.assertEqual(response, 'Error-1')

    def test_limitation_2(self):
        dict_filename = '{}/files/dictionary_words_limitation_2'.format(src_dir, )
        response = print_scramble_word_count(dict_filename, search_file)
        self.assertEqual(response, 'Error-2')

    def test_limitation_3(self):
        dict_filename = '{}/files/dictionary_words_limitation_3'.format(src_dir, )
        response = print_scramble_word_count(dict_filename, search_file)
        self.assertEqual(response, 'Error-3')


if __name__ == '__main__':
    unittest.main()
