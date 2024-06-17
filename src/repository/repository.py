from typing import TypeVar, Generic, List

from sqlalchemy.orm import Session

T = TypeVar('T')


class BaseRepo:

    @staticmethod
    def retrieve_all(db: Session, model: Generic[T]):
        return db.query(model).all()

    @staticmethod
    def retrieve_by_id(db: Session, model: Generic[T], id: int):
        return db.query(model).filter(model.id == id).all()

    @staticmethod
    def retrieve_by_first_id(db: Session, model: Generic[T], id: int):
        return db.query(model).filter(model.id == id).first()

    @staticmethod
    def insert(db: Session, model: Generic[T]):
        db.add(model)
        db.commit()
        db.refresh(model)

    @staticmethod
    def update(db: Session, model: Generic[T]):
        db.commit()
        db.refresh(model)

    @staticmethod
    def delete(db: Session, model: Generic[T]):
        db.delete(model)
        db.commit()

    @staticmethod
    def bulk(db: Session, models: List[Generic[T]]):
        db.bulk_save_objects(models)
        db.commit()


class ViniDataRepository(BaseRepo):
    pass
