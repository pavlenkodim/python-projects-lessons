import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers={'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org) generic-library/0.0',
                                             'Content-Type': 'text/html'}) as response:
            html = await response.text()
            return html

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    # for link in soup.find_all('a'):
    #     if link['href'].startswith('https://'):
    #         print(link['href'])
    #
    # # print(soup.prettify())

    # for image in soup.find_all('img'):
    #     if image['src'].startswith('//'):
    #         url = 'https:' + image['src']
    #         match = re.search(r"\.([^.]+)$", url)
    #         if match:
    #             extension = match.group(1)
    #             save_image(url, image['alt'] + '.' + extension)

    out_text = open('wiki.txt', 'w', encoding='utf-8')
    for string in soup.strings:
        if string == '\n':
            continue
        out_text.write(html)
    out_text.close()

async def main():
    html = await fetch_html('https://en.wikipedia.org/wiki/Python_(programming_language)')
    parse_html(html)

asyncio.run(main())

