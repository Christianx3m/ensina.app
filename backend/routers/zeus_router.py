from fastapi import APIRouter, Body
from openai import OpenAI
from dotenv import load_dotenv
import os
from prompts.zeus_prompt import ZEUS_PERSONALITY

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
router = APIRouter(prefix="/zeus", tags=["Zeus"])

@router.get("/")
def zeus_home():
    return {"zeus": "Sim, eu sou Zeus. E não, não é simples ser um mentor tão sábio."}

@router.post("/ask")
def ask_zeus(payload: dict = Body(...)):
    question = payload.get("question", "")
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": ZEUS_PERSONALITY},
            {"role": "user", "content": question}
        ]
    )
    answer = completion.choices[0].message.content
    return {"zeus": answer}