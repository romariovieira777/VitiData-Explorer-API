from fastapi import APIRouter, Depends
from starlette.requests import Request

from src.repository.repository import JWTBearer
from src.schema.schema import ResponseSchema
from src.service.service import ExportWineService, ExportSparklingService, ExportGrapeService, ExportJuiceService

router = APIRouter()


@router.get("/update/table/export/wine", dependencies=[Depends(JWTBearer())])
async def update_table_export_wine(request: Request):
    try:
        export_wine_service = ExportWineService()

        export_wine_service.update_table_exp_wine()

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


@router.get("/update/table/export/sparkling", dependencies=[Depends(JWTBearer())])
async def update_table_export_sparkling(request: Request):
    try:
        export_sparkling_service = ExportSparklingService()

        export_sparkling_service.update_table_exp_sparkling()

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


@router.get("/update/table/export/grape", dependencies=[Depends(JWTBearer())])
async def update_table_export_grape(request: Request):
    try:
        export_grape_service = ExportGrapeService()

        export_grape_service.update_table_exp_grape()

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


@router.get("/update/table/export/juice", dependencies=[Depends(JWTBearer())])
async def update_table_export_juice(request: Request):
    try:
        export_juice_service = ExportJuiceService()

        export_juice_service.update_table_exp_juice()

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