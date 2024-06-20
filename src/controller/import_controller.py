from fastapi import APIRouter, Depends
from starlette.requests import Request

from src.repository.repository import JWTBearer
from src.schema.schema import ResponseSchema
from src.service.service import ImportWineService, ImportSparklingService, ImportFreshGrapeService, \
    ImportDriedGrapesService, ImportJuiceService

router = APIRouter()


@router.get("/update/table/import/wine", dependencies=[Depends(JWTBearer())])
async def update_table_import_wine(request: Request):
    try:
        import_wine_service = ImportWineService()

        import_wine_service.update_table_imp_wine()

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


@router.get("/update/table/import/sparkling", dependencies=[Depends(JWTBearer())])
async def update_table_import_sparkling(request: Request):
    try:
        import_sparkling_service = ImportSparklingService()

        import_sparkling_service.update_table_imp_sparkling()

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


@router.get("/update/table/import/fresh/grape", dependencies=[Depends(JWTBearer())])
async def update_table_import_fresh_grape(request: Request):
    try:
        import_fresh_grape_service = ImportFreshGrapeService()

        import_fresh_grape_service.update_table_imp_fresh_grapes()

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

@router.get("/update/table/import/dried/grapes", dependencies=[Depends(JWTBearer())])
async def update_table_import_dried_grapes(request: Request):
    try:
        import_dried_grapes_service = ImportDriedGrapesService()

        import_dried_grapes_service.update_table_imp_dried_grapes()

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

@router.get("/update/table/import/juice", dependencies=[Depends(JWTBearer())])
async def update_table_import_juice(request: Request):
    try:
        import_juice_service = ImportJuiceService()

        import_juice_service.update_table_imp_juice()

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