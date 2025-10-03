from fastapi import FastAPI

app = FastAPI(title="AI Generated Finance App - Stub")

@app.get("/health")
async def health():
    return {"status": "ok"}

