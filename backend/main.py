import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from fastapi.openapi.docs import get_swagger_ui_html

# 🔧 Carrega variáveis do ambiente
load_dotenv()
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# 🔹 Importa os routers dos agentes
from routers import core_router
from routers.zeus_router import router as zeus_router
from routers.gaia_router import router as gaia_router
from routers.pulga_router import router as pulga_router
from routers.xavier_router import router as xavier_router
from routers.repi_router import router as repi_router

# 🚀 Inicializa a aplicação
app = FastAPI(
    title="Ensina.app API",
    version="0.1.0",
    description="Backend dos agentes Zeus, Gaia, Pulga, Xavier e REPI."
)

# 🌐 Endpoint principal
@app.get("/")
def root():
    return {"status": "AutoDev backend online", "debug_mode": DEBUG}

# 🗂️ Servir arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# 📘 Swagger UI padrão
@app.get("/docs", include_in_schema=False)
async def default_docs():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title,
        swagger_favicon_url="https://fastapi.tiangolo.com/img/favicon.png",
    )

# 🤖 Routers dos agentes
app.include_router(zeus_router)
app.include_router(gaia_router)
app.include_router(pulga_router)
app.include_router(xavier_router)
app.include_router(repi_router)
app.include_router(core_router.router)
