from fastapi import FastAPI
from routers import core_router
from routers.zeus_router import router as zeus_router
from routers.gaia_router import router as gaia_router
from routers.pulga_router import router as pulga_router
from routers.xavier_router import router as xavier_router

app = FastAPI(title="ensina.app API", version="0.1.0")

@app.get("/")
def root():
    return {"status": "AutoDev backend online"}

# Inclui os routers
app.include_router(zeus_router)
app.include_router(gaia_router)
app.include_router(pulga_router)
app.include_router(xavier_router)
app.include_router(core_router.router)
