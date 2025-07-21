from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db_models.database import get_db_session
from app.db_models.haunted_location import HauntedLocation
from app.services.haunted_location_service import HauntedLocationService
from app.schemas.haunted_location_out import HauntedLocationOut
from app.schemas.haunted_location_in import HauntedLocationIn

router = APIRouter()


@router.get("/haunted_locations/")
def get_all_haunted_locations(
    session: Session = Depends(get_db_session),
) -> list[HauntedLocationOut]:
    service = HauntedLocationService(session=session)
    return service.get_all()


@router.post("/haunted_locations/")
def create_haunted_location(
    haunted_location_in: HauntedLocationIn, session: Session = Depends(get_db_session)
) -> HauntedLocationOut:
    service = HauntedLocationService(session=session)
    haunted_location = HauntedLocation(
        title=haunted_location_in.title, description=haunted_location_in.description
    )
    created_haunted_location = service.create(haunted_location)
    return HauntedLocationOut(
        id=created_haunted_location.id,
        title=created_haunted_location.title,
        description=created_haunted_location.description,
    )
