from fastapi import APIRouter, Depends
from starlette.requests import Request
from src.repository.repository import JWTBearer
from src.schema.schema import ResponseSchema

router = APIRouter()


@router.get("/production/all", dependencies=[Depends(JWTBearer())])
async def get_productions_all(request: Request):
    try:
        return ResponseSchema(
            code="200",
            status="Ok",
            message="Success retrieve data",
            result=""
        ).dict(exclude_none=True)
    except Exception as e:
        return ResponseSchema(
            code="500",
            status="Error",
            message=e.__str__()
        ).dict(exclude_none=True)
