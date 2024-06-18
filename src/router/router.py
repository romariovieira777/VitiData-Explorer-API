from fastapi import APIRouter
from src.controller import auth_controller, commercialization_controller, export_controller, import_controller, processing_controller, production_controller

router = APIRouter()

router.include_router(auth_controller.router, prefix='/api/vitidata/auth', tags=['Authentication'])
router.include_router(commercialization_controller.router, prefix='/api/vitidata', tags=['Commercialization'])
router.include_router(export_controller.router, prefix='/api/vitidata', tags=['Export'])
router.include_router(import_controller.router, prefix='/api/vitidata', tags=['Import'])
router.include_router(production_controller.router, prefix='/api/vitidata', tags=['Production'])
router.include_router(processing_controller.router, prefix='/api/vitidata', tags=['Processing'])

