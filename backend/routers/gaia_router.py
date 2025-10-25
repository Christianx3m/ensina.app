from fastapi import APIRouter, Body
import io, contextlib

router = APIRouter(prefix="/gaia", tags=["Gaia"])

@router.get("/")
def gaia_home():
    return {"gaia": "Sou Gaia, a executora. Vamos transformar ideias em ação."}

@router.post("/run")
def run_code(payload: dict = Body(...)):
    code = payload.get("code", "")
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            exec(code, {})
        result = output.getvalue()
    except Exception as e:
        result = f"Erro ao executar: {str(e)}"
    return {"gaia_result": result}
