from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"status": "AutoDev backend online"}

@app.post("/zeus/ask")
def ask_zeus(data: Question):
    """
    Zeus responde perguntas sobre programação e aprendizado de forma didática.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é Zeus, um mentor experiente que ensina programação de forma clara e paciente."},
                {"role": "user", "content": data.question}
            ]
        )
        return {"zeus": response.choices[0].message.content}

    except Exception as e:
        return {"error": str(e)}