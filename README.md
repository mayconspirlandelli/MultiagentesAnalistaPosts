# MultiagentesAnalistaPosts
Prototipo de Multigentes  responsável por Analisar Publicações das Mídias Sociais com conteúdo de desinformação e Fake News.

# Agora vamos usar documetncao do CrewAI
curl -LsSf https://astral.sh/uv/install.sh | sh

https://docs.crewai.com/installation


# Aula 01 Parte 3 no minuto 58min explica como criar o projeto Crewai
# Usar o gerenciador de bibliotecas do Python UV
# Para MacOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install CrewAI
uv tool install crewai

# Verificar instalação 
uv tool list

# Crie a pasta do projeto. Dentro da pasta voce digita o comando. O projeto é inicializado com nome da pasta.
uv init 

# Vamos adicionar o crewai aqui no projeto. Ele criva o ambiente virutal do python ".venv" de forma automática. Crai a Toml e Lock
uv add crewai

# No arquivo "main.py" apague tudo e crie com novo. 
from crewai import Agent

# Instalar o Tools
uv add crewai-tools

# Instalar dotenv
uv add python-dotenv

