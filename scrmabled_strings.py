import argparse


def check_similarity(wrd_chars, srch_wrd_chars):
    if len(wrd_chars) >= len(srch_wrd_chars):
        ref_lst, trgt_lst = wrd_chars, srch_wrd_chars
    else:
        ref_lst, trgt_lst = srch_wrd_chars, wrd_chars
    for char in ref_lst:
        if char not in trgt_lst:
            return False
    return True


def word_check(dict_wrd, srch_wrd, ):
    flag = False
    wl = len(dict_wrd)
    f, l = dict_wrd[0], dict_wrd[wl - 1]
    g = wl - 1
    wuc = set([c for c in dict_wrd[1:-1]])
    for i, c in enumerate(srch_wrd):
        if i + g > len(srch_wrd) - 1:
            flag = False
            break
        if c == f and srch_wrd[i + g] == l:
            suc = set([c for c in srch_wrd[i + 1:i + g]])
            if len(wuc) == len(suc):
                flag = check_similarity(wuc, suc)
            if flag:
                break
    return flag


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
            if word_len > 105 or word_len < 2:
                print('Each word in the dictionary is between 2 and 105 letters long, inclusive.')
                return 'Error-2'
            dict_words_len += word_len
        if dict_words_len > 105:
            print('The sum of lengths of all words in the dictionary does not exceed 105.')
            return 'Error-3'
        for line_index, line in enumerate(ser_strs):
            line_index += 1
            counter = 0
            for word in dict_words:
                if word_check(word, line):
                    counter += 1
            print('Case #{}: {}'.format(line_index, counter))
    except Exception as e:
        print('Process flow got interrupted due to {}'.format(e))


# Process starts here..!!
# import time

if __name__ == '__main__':
    # curr_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument("--dictionary")
    parser.add_argument("--input")
    args = parser.parse_args()
    print_scramble_word_count(args.dictionary, args.input)
    # print('Total time {} sec'.format(round(time.time() - curr_time), 2))
