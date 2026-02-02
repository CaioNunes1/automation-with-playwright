import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/radio-button")

        #actions
        await page.locator("label[for='yesRadio']").click()
        await expect(page.locator("#mt-3")).to_have_text("You have selected")
        await expect(page.locator("#text-sucess")).to_have_text("Yes")

asyncio.run(main())