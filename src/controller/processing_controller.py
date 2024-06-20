from fastapi import APIRouter, Depends
from starlette.requests import Request

from src.repository.repository import JWTBearer
from src.schema.schema import ResponseSchema
from src.service.service import ProcessingViniferasService, ProcessingAmericanAndHybridService, \
    ProcessingTableGrapesService, ProcessingClassLessService

router = APIRouter()


@router.get("/update/table/processing/viniferas", dependencies=[Depends(JWTBearer())])
async def update_table_processing_viniferas(request: Request):
    try:
        processing_viniferas_service = ProcessingViniferasService()

        processing_viniferas_service.update_table_process_viniferas()

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


@router.get("/update/table/processing/american/hybrid", dependencies=[Depends(JWTBearer())])
async def update_table_processing_american_hybrid(request: Request):
    try:
        processing_american_hybrid_service = ProcessingAmericanAndHybridService()

        processing_american_hybrid_service.update_table_process_american_and_hybrid()

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


@router.get("/update/table/processing/table/grapes", dependencies=[Depends(JWTBearer())])
async def update_table_processing_table_grapes(request: Request):
    try:
        processing_table_grapes_service = ProcessingTableGrapesService()

        processing_table_grapes_service.update_table_process_table_grapes()

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



@router.get("/update/table/processing/class/less", dependencies=[Depends(JWTBearer())])
async def update_table_processing_american_hybrid(request: Request):
    try:
        processing_class_less_service = ProcessingClassLessService()

        processing_class_less_service.update_table_process_class_less()

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