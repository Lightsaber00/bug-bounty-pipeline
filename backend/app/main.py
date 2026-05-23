from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Bug Bounty Pipeline API",
    version="0.1.0",
    description="API skeleton for a recon, scan, validate, and report workflow."
)

class HealthResponse(BaseModel):
    status: str
    service: str

@app.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(status="ok", service="bug-bounty-pipeline")

@app.get("/api/v1/summary")
def summary():
    return {
        "project": "Bug Bounty Pipeline",
        "mode": "skeleton",
        "message": "Replace mocked handlers with real recon, scan, validation, and reporting logic."
    }
