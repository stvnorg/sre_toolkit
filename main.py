from fastapi import FastAPI
from routers import net

app = FastAPI()

app.include_router(net.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
