from pydantic import BaseModel


class HauntedLocationIn(BaseModel):
    title: str
    description: str
