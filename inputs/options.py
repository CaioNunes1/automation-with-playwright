import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/select-menu")

        await page.locator("text=Select Option").click()
        await page.locator("text=Select Option").click()

        #actions
        await page.select_option("select#cars",["Volvo","Opel","Audi"])
        await page.screenshot(path="screenshots/multiselect.png")

        #stopping tracing
        await context.tracing.stop(path="logs/traceoption.zip")
        await browser.close()

asyncio.run(main())