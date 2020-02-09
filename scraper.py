import requests
import argparse
import os
from bs4 import BeautifulSoup


base_url = 'https://kisslightnovels.info/novel'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=(''))
    # The following argument(s) should be provided to run this script.
    parser.add_argument('-u', '--uri', type=str, required=True, help='Name of the novel in the url')
    parser.add_argument('-c', '--chapters', type=str, required=True, help='Number of chapters.')

    args = parser.parse_args()

    print('Starting...', end='\n\n')

    print('Creating directory...')
    try:
        os.mkdir(args.uri)
        os.chdir(args.uri)
    except FileExistsError as e:
        os.chdir(args.uri)

    for i in range(1, 1 + int(args.chapters)):
        url = f'{base_url}/{args.uri}/{args.uri}-chapter-{i}/'
        
        print(f'Accessing url {url}')

        html = requests.get(url)
        if html.status_code == 404:
            print('The server could not be found!')
            break

        bs = BeautifulSoup(html.text, 'lxml')
        
        chapter = bs.find('div', class_='reading-content').text.replace(' .', '.').replace('\n\n\r\n     (adsbygoogle = window.adsbygoogle || []).push({});\r\n\n', '')
        filename = f'chapter-{i}.txt'
        
        print('Generating txt file...')
        
        file = open(filename,"w")
        file.write(chapter)
        file.close()
        
        print(f'{filename} saved successfully!', end='\n\n')

    print('# Finished')