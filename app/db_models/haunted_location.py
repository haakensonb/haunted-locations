from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, timestamp


class HauntedLocation(Base):
    __tablename__ = "haunted_location"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(5000))
    created_at: Mapped[timestamp] = mapped_column()
