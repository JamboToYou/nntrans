#!/usr/bin/env python3
import asyncio

import aiofiles
import aiohttp

MAX_SIZE = 4800


async def translate(entry):
    body = {
        'text': entry,
        'gfrom': 'ru',
        'gto': 'uz',
        'key': '2956684590ru85'
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('https://www.webtran.ru/gtranslate/',
                                data=body) as response:
            return await response.text()


async def main():
    with open('dataset/splitted_by_regexp.txt', 'r') as fin:
        sentences = fin.readlines()
    async with aiofiles.open('dataset/dataset_by_regexp_result.txt', 'w') as fout:
        for line in sentences:
            translation = await translate(line)
            print(f'[Done] chunk {translation}')
            final_sentence = f"{line}\t{translation}"
            await fout.write(final_sentence)
            await fout.flush()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
