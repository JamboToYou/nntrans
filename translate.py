#!/usr/bin/env python3
import re

from requests import post

MAX_SIZE = 4800

def translate(entry):
    body = {
        'text': entry,
        'gfrom': 'ru',
        'gto': 'uz',
        'key': '2956684590ru85'
    }
    result = post('https://www.webtran.ru/gtranslate/', data=body)
    return result.text


def split_to_sentence_chunks(sentences, max_size):
    result = []
    chunk = []
    for sentence in sentences:
        if sum([len(sent) for sent in chunk]) + len(sentence) < max_size:
            chunk.append(sentence)
        elif len(sentence) > max_size:
            print('Long sentence found')
            pass
        else:
            result.append(''.join(chunk))
            chunk = []
    if chunk != []:
        result.append(''.join(chunk))
    return result


# def splitkeepsep(s, sep): return reduce(lambda acc, elem: acc[:-1] + [acc[-1] + elem] if elem == sep else acc + [elem], re.split("(%s)" % re.escape(sep), s), [])


# if __name__ == '__main__':
#     filenames = [entry for entry in listdir(INPUT_DIR) if isfile('/'.join((abspath(INPUT_DIR), entry)))]
#     for filename in filenames:
#         src_path = '/'.join((abspath(INPUT_DIR), filename))
#         dest_path = '/'.join((abspath(OUTPUT_DIR), filename))
#         translation = ''
#         filetext = ''

#         print('[INFO]: Processing file ' + filename + '. . .')
#         print('[INFO]: in : ' + src_path)
#         print('[INFO]: out: ' + dest_path)
#         with open(src_path, 'r') as fin:
#             filetext = fin.read().replace('\n', ' ')

#         for chunk in split_to_sentence_chunks(filetext, MAX_SIZE):
#             translation += ' '
#             translation += translate(chunk).replace('\n', ' ')

#         with open(dest_path, 'w') as fout:
#             fout.write(translation)
#         print('[INFO]: Done with ' + filename)

if __name__ == "__main__":
    sentences = []
    with open('dataset/norm.txt', 'r') as fin:
        sentences = fin.readlines()

    with open('dataset/dataset1.txt', 'w') as fout:
        for i, chunk in enumerate(split_to_sentence_chunks(sentences, MAX_SIZE)):
            translation = translate(chunk)
            sents1 = chunk.split('\n')
            sents2 = translation.split('\n')
            if len(sents1) == len(sents2):
                print('eq')
                fout.writelines(['\t'.join(s) for s in zip((sents1, sents2))])
            else:
                print(f'not eq: {len(sents1)} - {len(sents2)}')
                # print(f'[] {chunk} - {translation}')
            # fout.write()
            print(f'[Done] chunk {i}')
