from fastapi import APIRouter
from prompts import xavier_prompt

router = APIRouter(
    prefix="/xavier",
    tags=["👨‍🏫 Professor Xavier"]
)

@router.get("/", summary="Introdução do Professor Xavier")
def xavier_info():
    return {
        "personagem": "Professor Xavier",
        "personalidade": xavier_prompt.get_personality(),
        "mensagem": "Sou o Professor Xavier, diretor do Ensina.app. Supervisionei Zeus, Gaia e Pulga — e oriento você a pensar com clareza."
    }
