from crewai import Agent, Task, Crew, LLM, Process
from dotenv import load_dotenv
import os
from tools.instagram_tools import InstagramScraperTool

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()  # Isso carrega as variáveis do .env para os.environ

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0,
    api_key=GOOGLE_API_KEY,
)

instagram_reader = Agent(
    role="Leitor de Instagram",
    goal="Ler conteúdo da página do Instagram Web",
    backstory="Especialista em extrair informações visuais de páginas web do Instagram",
    tools=[InstagramScraperTool()],
    verbose=True
)

task = Task(
    description="Leia os primeiros comentários do último post do perfil @inf.ufg",
    expected_output="Lista dos primeiros 5 comentários",
    agent=instagram_reader,
    verbose=True,
    memory=True,
    llm=llm
)

crew = Crew(
    agents=[instagram_reader],
    tasks=[task],
    process=Process.sequential,
    llm=llm,
    verbose=True
)

# Executar
resultado = crew.kickoff()
print(resultado)

# output = crew.run()
# print(output)
