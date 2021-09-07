from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from routers import tools

app = FastAPI()

app.include_router(tools.router)

Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"name": "sre-toolkit"}
