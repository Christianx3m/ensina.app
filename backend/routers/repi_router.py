from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from uuid import uuid4
from prompts import repi_prompt

router = APIRouter(
    prefix="/repi",
    tags=["📁 REPI"]
)

# Armazenamento em memória (apenas para testes locais)
_PLANS: Dict[str, Dict[str, Any]] = {}

@router.get("/", summary="Introdução da REPI")
def repi_info():
    return {
        "agente": "REPI",
        "missao": repi_prompt.get_personality(),
        "mensagem": (
            "Sou a REPI. Registro planos, histórico e documentos do aluno. "
            "Posso receber um plano do Xavier e devolvo um ID para consulta."
        )
    }

# ---- Modelos de dados para o plano de estudo ----
class Module(BaseModel):
    title: str = Field(..., description="Título do módulo")
    eta_days: int = Field(..., ge=1, description="Tempo estimado em dias")
    resources: Optional[List[str]] = Field(default=None, description="Links ou referências opcionais")

class LearningPlan(BaseModel):
    tenant_id: Optional[str] = Field(default="default", description="Identificador do tenant (multi-tenant)")
    student_id: str = Field(..., description="ID do aluno")
    goal: str = Field(..., description="Objetivo do aluno / projeto")
    difficulty: Optional[str] = Field(default=None, description="Dificuldade estimada (ex.: fácil/médio/difícil)")
    modules: List[Module] = Field(..., description="Lista de módulos do plano")

class PlanAck(BaseModel):
    plan_id: str
    status: str
    message: str

@router.post("/register_plan", response_model=PlanAck, summary="Registrar plano de estudo enviado pelo Xavier")
def register_plan(plan: LearningPlan):
    """
    Recebe um plano de estudo (normalmente gerado pelo Xavier) e registra para consulta.
    Neste MVP, armazena em memória. Em breve: persistência (Postgres/Supabase) e geração de documentos.
    """
    plan_id = str(uuid4())
    _PLANS[plan_id] = plan.model_dump()
    return PlanAck(
        plan_id=plan_id,
        status="registered",
        message="Plano registrado pela REPI com sucesso."
    )

@router.get("/plans/{plan_id}", summary="Obter um plano de estudo registrado")
def get_plan(plan_id: str):
    plan = _PLANS.get(plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    return {"plan_id": plan_id, "plan": plan}
