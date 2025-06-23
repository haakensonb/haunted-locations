from fastapi import APIRouter

router = APIRouter()


@router.get("/haunted_locations/")
def read_haunted_locations():
    return "Spooky haunted"
