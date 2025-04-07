from playwright.sync_api import sync_playwright
#usando o gerenciador de contexto para garantir que o Playwright 
#seja corretamente iniciado e encerrado (tipo um try/finally por baixo dos panos).
with sync_playwright() as p: # gerenciador de contexto em Python,
    browser = p.edgechromium.launch() #abrindo o edge chromium
    page = browser.new_page() #abrndo uma nova aba
    page.goto("")#navegando na url passada