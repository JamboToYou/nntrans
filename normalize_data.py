#!/usr/bin/env python3

import os
import re
import sys

INPUT_DIR = sys.argv[1]
# OUTPUT_DIR = sys.argv[2]

SENTENCE_REGEXP = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)"


def split_to_sentences(text):
    return re.split(SENTENCE_REGEXP, text)


if __name__ == '__main__':
    filenames = os.listdir(INPUT_DIR)
    with open('dataset/splitted_by_regexp.txt', 'w') as fout:
        for filename in filenames:
            with open(f'{INPUT_DIR}/{filename}', 'r') as file:
                # with open('dataset/unnorm.txt', 'r') as file:
                filetext = re.sub(' +', ' ', file.read())

            filetext = filetext.replace('\n', '')
            filetext = filetext.replace('\t', '')

            filetext = '\n'.join([sent.strip() for sent in split_to_sentences(filetext)])
            print(filetext)

            fout.write(filetext)
            # break
