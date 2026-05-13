# AI-Powered PCI DSS & Microsoft 365 Audit Assistant

Production-ready starter architecture for a compliance-focused audit platform.

## Stack
- Frontend: React + TypeScript + Vite + Tailwind CSS
- Backend: FastAPI + SQLAlchemy + SQLite (PostgreSQL-ready)
- Auth: JWT scaffold with RBAC hooks
- Infra: Docker Compose

## Features (Starter)
- PCI DSS dashboard
- Microsoft 365 posture page
- Evidence upload page
- Audit findings table
- Admin panel
- RBAC scaffold
- Wazuh integration placeholder
- Microsoft Graph integration placeholder
- PDF report placeholder

## Quick Start
```bash
docker compose up --build
```

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Local Development
### Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
