import itertools
import argparse


def split(word):
    return [char for char in word]


def permute_v2(word):
    mdle_wrds = set([''.join(val) for val in set(itertools.permutations(split(word[1:-1])))])
    final_words = ['{0}{1}{2}'.format(word[0], wrd, word[len(word) - 1]) for wrd in mdle_wrds] + [
        '{2}{1}{0}'.format(word[0], wrd, word[len(word) - 1]) for wrd in mdle_wrds]
    return set(final_words)


def print_scramble_word_count(dict_file, ser_str_file):
    try:
        with open(ser_str_file) as fp:
            ser_strs = fp.readlines()

        with open(dict_file) as fp:
            dict_words = [word.strip() for word in fp.readlines()]

        if len(dict_words) != len(set(dict_words)):
            print('No two words in the dictionary are the same.')
            return 'Error-1'

        dict_words_len = 0
        for word in dict_words:
            word_len = len(word)
            if 105 < word_len < 2:
                print('Each word in the dictionary is between 2 and 105 letters long, inclusive.')
                return 'Error-2'
            dict_words_len += word_len

        if dict_words_len > 105:
            print('The sum of lengths of all words in the dictionary does not exceed 105.')
            return 'Error-3'

        for line_index, ser_str in enumerate(ser_strs):
            line_index += 1
            counter = 0
            for word in dict_words:
                scrmb_word_set = permute_v2(word, )
                for wrd in scrmb_word_set:
                    if wrd in ser_str:
                        counter += 1
            print('Case #{}: {}'.format(line_index, counter))
    except Exception as e:
        print('Process flow got interrupted due to {}'.format(e))


# Process starts here..!!
parser = argparse.ArgumentParser()
parser.add_argument("--dictionary")
parser.add_argument("--input")
args = parser.parse_args()

print_scramble_word_count(args.dictionary, args.input)
