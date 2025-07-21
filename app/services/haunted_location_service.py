from app.interfaces.repo_service import RepoService
from app.db_models.haunted_location import HauntedLocation
from sqlalchemy.orm import Session
from sqlalchemy import select


class HauntedLocationService(RepoService[HauntedLocation]):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, entity: HauntedLocation) -> HauntedLocation:
        self.session.add(entity)
        self.session.commit()
        return entity

    def get_all(self) -> list[HauntedLocation]:
        stmt = select(HauntedLocation)
        return self.session.scalars(stmt).all()
