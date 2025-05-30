from crewai.tools import BaseTool
# from crewai import BaseTool
from dotenv import load_dotenv
import google.generativeai as genai
import os
from PIL import Image

# Carregar variáveis de ambiente do arquivo .env
load_dotenv() 
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configurar Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Criar a Tool
class GeminiVisionTool(BaseTool):
    name = "GeminiVisionTool"
    description = "Interpreta visualmente um print do Instagram"

    def _run(self, input_image_path: str) -> str:
        image = Image.open(input_image_path)
        prompt = "Descreva o conteúdo do post do Instagram com base na imagem"
        
        model = genai.GenerativeModel("gemini-pro-vision")
        response = model.generate_content([prompt, image])
        return response.text
