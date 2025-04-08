from playwright.sync_api import sync_playwright
import time
#usando o gerenciador de contexto para garantir que o Playwright 
#seja corretamente iniciado e encerrado (tipo um try/finally por baixo dos panos).
with sync_playwright() as p: # gerenciador de contexto em Python,
    browser = p.chromium.launch(headless=False) #abrindo o edge chromium, o headless é para abrir o browser e mostrar, não ficar invisível
    page = browser.new_page() #abrndo uma nova aba
    page.goto("http://google.com")#navegando na url passada
    page.screenshot(path="screenshot.png") #tirando o screenshot da página
    time.sleep(5)
    browser.close()
    