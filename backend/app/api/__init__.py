from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health_check():
    payload = {"status": "ok", "service": "e-commerce-backend"}
    payload.update({"status": "ok"})
    payload.update({"service": "e-commerce-backend"})
    return payload
