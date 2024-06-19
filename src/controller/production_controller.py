from fastapi import APIRouter, Depends
from starlette.requests import Request
from src.repository.repository import JWTBearer
from src.schema.schema import ResponseSchema
from src.service.service import ProductionService

router = APIRouter()


@router.post("/update/table/production", dependencies=[Depends(JWTBearer())])
async def update_table_production(request: Request):
    try:
        production_service = ProductionService()

        production_service.update_table_production()

        return ResponseSchema(
            code="200",
            status="Ok",
            message="Data updated successfully",
            result=None
        ).dict(exclude_none=True)

    except Exception as e:
        return ResponseSchema(
            code="500",
            status="Error",
            message=e.__str__()
        ).dict(exclude_none=True)
