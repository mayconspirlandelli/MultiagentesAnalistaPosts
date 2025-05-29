#from crewai.tools import BaseTool
#from crewai_tools import BaseTool
from crewai.tools import tool
#from crewai import Tool
# from crewai.tools import BaseTool
from playwright.sync_api import sync_playwright, Playwright


# from playwright.sync_api import sync_playwright, Playwright

# def run(playwright: Playwright):
#     chromium = playwright.chromium # or "firefox" or "webkit".
#     browser = chromium.launch()
#     page = browser.new_page()
#     page.goto("http://example.com")
#     # other actions...
#     browser.close()

# with sync_playwright() as playwright:
#     run(playwright)
    
    

# class InstagramScraperTool(BaseTool):
#     name = "InstagramScraperTool"
#     description = "Extrai informações da interface web do Instagram"

    # def run(playwright: Playwright) -> str:
        
    #         browser = playwright.chromium.launch(headless=False)
    #         context = browser.new_context()
    #         page = context.new_page()
    #         page.goto("https://www.instagram.com")

    #         input("Faça login e pressione Enter para continuar...")

    #         page.wait_for_timeout(5000)  # Espera carregar
    #         page.goto("https://www.instagram.com/inf.ufg/")
    #         page.wait_for_timeout(3000)

    #         # Exemplo: extrair o texto dos comentários do primeiro post
    #         post = page.locator('article').nth(0)
    #         post.click()
    #         page.wait_for_timeout(2000)

    #         comments = page.locator('[role="dialog"] ul li span').all_inner_texts()
    #         print(f"Total de comentários encontrados: {len(comments)}")

    #         browser.close()
    #         #return comments[:5]  # Retorna os primeiros 5 comentários
            
            
#     with sync_playwright() as playwright:
#         run(playwright)
#             # primeiros_comentarios = comments[:5]
#             # texto_formatado = "\n".join(primeiros_comentarios)
#             # return texto_formatado


#             #return "\n".join(comments[:5])





class InstagramScraperTool(tool):
    name = "InstagramScraperTool"
    description = "Extrai informações da interface web do Instagram"


    #def _run() -> str:
    def run(playwright: Playwright) -> str:
        
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.instagram.com")

        input("Faça login e pressione Enter para continuar...")

        page.wait_for_timeout(5000)  # Espera carregar
        page.goto("https://www.instagram.com/nome_do_perfil/")
        page.wait_for_timeout(3000)

        # Exemplo: extrair o texto dos comentários do primeiro post
        post = page.locator('article').nth(0)
        post.click()
        page.wait_for_timeout(2000)

        comments = page.locator('[role="dialog"] ul li span').all_inner_texts()
        print(f"Total de comentários encontrados: {len(comments)}")
        browser.close()

        primeiros_comentarios = comments[:5]
        texto_formatado = "\n".join(primeiros_comentarios)
        return texto_formatado

    with sync_playwright() as playwright:
        run(playwright)            
