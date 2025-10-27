from fastapi import APIRouter
from pydantic import BaseModel
from utils import xavier_engine
import uuid

router = APIRouter(
    prefix="/xavier",
    tags=["👨‍🏫 Professor Xavier"]
)

class ProjectRequest(BaseModel):
    descricao: str

class AnswerRequest(BaseModel):
    session_id: str
    resposta: str

@router.post("/analyze_project", summary="Analisa o projeto inicial do aluno")
async def analyze_project(request: ProjectRequest):
    """
    Cria uma nova sessão de aprendizado com base na descrição do projeto.
    """
    session_id = str(uuid.uuid4())
    result = xavier_engine.start_session(session_id, request.descricao)
    return result

@router.post("/answer", summary="Continua a conversa com o Professor Xavier")
async def continue_conversation(request: AnswerRequest):
    """
    Continua uma sessão de conversa já iniciada.
    """
    result = xavier_engine.continue_session(request.session_id, request.resposta)
    return result
