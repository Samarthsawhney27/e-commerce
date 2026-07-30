# Demo E-Commerce Application

A small but realistic e-commerce application demonstrating a typical microservice-oriented monorepo. This project is intended to be used as a target for deployment intelligence platforms like DeployIQ.

## Project Structure

- `frontend/`: React + TypeScript + Vite frontend.
- `backend/`: FastAPI Python backend.
- `payments/`: A standalone payments module.
- `auth/`: Authentication utilities and middleware.
- `database/`: SQL schemas and migrations.
- `docker/`: Docker configuration files (e.g. Nginx).

## How to Run

### Using Docker Compose (Recommended)

To start the entire stack (frontend, backend, and PostgreSQL database), run:

```bash
docker compose up -d
```

### Local Development

#### Start Frontend

```bash
cd frontend
npm install
npm run dev
```

#### Start Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```
