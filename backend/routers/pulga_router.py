from fastapi import APIRouter, Body
import re

router = APIRouter(prefix="/pulga", tags=["Pulga"])

@router.get("/")
def pulga_home():
    return {"pulga": "Sou a Pulga! Analiso seu código e aponto o que pode ser melhorado 🧐"}

@router.post("/evaluate")
def evaluate_code(payload: dict = Body(...)):
    code = payload.get("code", "")
    feedback = []

    # Regras básicas de avaliação
    if "print(" in code:
        feedback.append("💡 Considere usar logging em vez de print() para depuração profissional.")
    if "import *" in code:
        feedback.append("⚠️ Evite 'import *'. Isso pode causar conflitos e reduzir a legibilidade.")
    if len(code) < 10:
        feedback.append("🤔 Seu código parece muito curto, talvez precise de mais contexto.")
    if not feedback:
        feedback.append("✅ Seu código parece limpo e organizado. Muito bem!")

    return {"pulga_feedback": feedback}
