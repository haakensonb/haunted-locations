from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import DefaultTable


class HauntedLocation(DefaultTable):
    __tablename__ = "haunted_location"

    # id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(5000))
