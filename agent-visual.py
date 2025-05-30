from playwright.sync_api import sync_playwright

def capturar_post_instagram(url: str, output_file: str = "post.png"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)

        input("Faça login e pressione Enter para continuar...")
        page.wait_for_timeout(5000)

        # Screenshot da área do post
        post = page.locator("article").nth(0)
        post.screenshot(path=output_file)

        browser.close()
        return output_file




from crewai import Agent
from tools.gemini_vision_tool import GeminiVisionTool

vision_tool = GeminiVisionTool()

instagram_agent = Agent(
    role="Analista Visual de Instagram",
    goal="Interpretar visualmente posts do Instagram",
    backstory="Especialista em visão computacional, treinado para interpretar imagens de redes sociais.",
    tools=[vision_tool],
    verbose=True
)


from crewai import Task, Crew

imagem = capturar_post_instagram("https://www.instagram.com/p/DKHZC2qNEbO")

tarefa = Task(
    description=f"Analise visualmente o post capturado na imagem '{imagem}' e explique o que está sendo mostrado.",
    expected_output="Descrição detalhada da imagem",
    agent=instagram_agent
)

crew = Crew(agents=[instagram_agent], tasks=[tarefa], verbose=True)
output = crew.run()

print(output)
