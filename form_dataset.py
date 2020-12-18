#!/usr/bin/env python3

import sys
from os import listdir
from os.path import abspath, isfile

SENTENCE_DELIMETERS = ['.', '!', '?']

def split_to_sentences(text):
    sentences = []
    sentence = ''
    for ch in text:
        if ch in SENTENCE_DELIMETERS:
            sentences.append((sentence + ch).strip())
            sentence = ''
        else:
            sentence += ch
    return sentences

data_dir = sys.argv[1]

filenames = sorted(listdir('{}/input'.format(data_dir)))

with open('{}/dataset.txt'.format(data_dir), 'w') as dataset_file:
    for filename in filenames:

        input_file_text = ''
        target_file_text = ''

        with open('{}/input/{}'.format(data_dir, filename), 'r') as f:
            input_file_text = f.read()
        with open('{}/target/{}'.format(data_dir, filename), 'r') as f:
            target_file_text = f.read()

        input_file_text.replace('\n', ' ')
        target_file_text.replace('\n', ' ')

        for pair in zip(split_to_sentences(input_file_text), split_to_sentences(target_file_text)):
            row = '\t'.join(pair) + '\n'
            if row.isspace():
                pass
            dataset_file.write(row)

# for i in range(10):
#     with open('{}/target/{}'.format(data_dir, filenames[i]), 'r') as f:
#         for sent in split_to_sentences(f.read()):
#             print(sent)