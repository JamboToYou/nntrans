#!/usr/bin/env python3

import os
import sys
import re

INPUT_DIR = sys.argv[1]
# OUTPUT_DIR = sys.argv[2]

SEPS = ['.', '!', '?']

def split_to_sentences(text):
    sentences = []
    sentence = ''
    first_sep = ''
    seps_row = False
    for ch in text:
        if ch in SEPS:
            if seps_row:
                pass
            else:
                first_sep = ch
                seps_row = True
        elif seps_row:
            seps_row = False
            sentences.append((sentence + first_sep).strip())
            sentence = ch
        else:
            sentence += ch
    sentences.append(sentence)
    return sentences

if __name__ == '__main__':
    filenames = os.listdir(INPUT_DIR)
    with open('dataset/norm.txt', 'a') as fout:
        for filename in filenames:
            filetext = ''

            with open(f'{INPUT_DIR}/{filename}', 'r') as fin:
            # with open('dataset/unnorm.txt', 'r') as fin:
                filetext = fin.read()

            # normalize sentence separators
            # filetext = re.sub(r'(\.|\?|\!|\n|\t| )+', r'\1', filetext)
            # remove newlines and tabulations
            filetext = filetext.replace('\n',' ')
            filetext = filetext.replace('\t',' ')

            filetext = '\n'.join([sent for sent in split_to_sentences(filetext) if len(sent) > 20])
            # print(filetext)

            fout.write(filetext)
            # break