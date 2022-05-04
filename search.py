#!/usr/local/bin/python3.9

import aiohttp
import asyncio
from hurry.filesize import size
from sys import argv


api_key = 'xj27ozhtcvjg45smvxb9uhbgetyj3ng3'
base_url = 'http://127.0.0.1:9117/'


async def search(query):

    async with aiohttp.ClientSession() as session:
        async with session.get(f'{base_url}api/v2.0/indexers/all/results?apikey={api_key}&Query={query}') as response:
            result_json = await response.json()
            return result_json['Results']


async def print_console(param):
    result_query = await search(param[1])

    #Only magnet
    struct = [ [{'Title': _['Title'], 'Seeders': _['Seeders'], 'MagnetUri': _['MagnetUri'], 'Size': size(_['Size'])}] for _ in result_query if _['Seeders'] != 0 and _['MagnetUri'] != None ]
    
    for _ in enumerate(struct):
        try:
            if _[0] >= int(param[2]):
                break
        except IndexError:
            if _[0] >= 10:
                break
     
        print(*_[1])

async def print_console_test():
    result_query = await search(param[1])
   
    print(result_query)


if __name__ == '__main__':
    try:
        asyncio.run(print_console_test(argv))
#        asyncio.run(print_console(argv))
    except IndexError:
        print('Чи шо ищем то?')
