import asyncio
from pyppeteer import launch

# https://pypi.org/project/pyppeteer/

URL = 'https://hk.appledaily.com/search/apple'


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(URL)

    await page.waitForSelector(".flex-feature")

    elements = await page.querySelectorAll('.flex-feature')

    for el in elements:
        text = await page.evaluate('(el) => el.textContent', el)
        print(text)

    await browser.close()


asyncio.get_event_loop().run_until_complete(main())