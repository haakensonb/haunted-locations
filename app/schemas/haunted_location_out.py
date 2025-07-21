from pydantic import BaseModel


class HauntedLocationOut(BaseModel):
    # TODO: replace id with uuid
    id: int
    title: str
    description: str
