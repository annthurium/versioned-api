from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/v0/fact/")
async def get_fact():
    return "President Coolidge had a pet raccoon named Rebecca"

@app.get("/v1/fact/")
async def get_fact():
    return "Raccoons are the cheapest mammals. A raccoon will use the same toothbrush for ten years rather than buy a new toothbrush."