from fastapi import FastAPI
from app.api.routes import auth, findings, health, integrations

app = FastAPI(title="Audit Assistant API")

app.include_router(health.router, prefix="/api")
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(findings.router, prefix="/api/findings", tags=["findings"])
app.include_router(integrations.router, prefix="/api/integrations", tags=["integrations"])
