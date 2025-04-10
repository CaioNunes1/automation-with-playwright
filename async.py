import asyncio
from playwright.async_api import async_playwright
import time

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Abrindo o Edge Chromium, o headless é para abrir o browser e mostrar, não ficar invisível
        page= await browser.new_page()
        await page.goto("http://whatsmyuseragent.org/")
        print(await page.title())
        time.sleep(10)
        await browser.close()


asyncio.run(main())
