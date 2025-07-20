from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import create_engine, DateTime, text
import datetime


# NOTE: This is only setup to work with Sqlite
class Base(DeclarativeBase):
    type_annotation_map = {datetime.datetime: DateTime(timezone=True)}


class DefaultTable(Base):
    __tablename__ = "default_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at = mapped_column(
        DateTime(timezone=True), server_default=text("(datetime('now'))")
    )
    updated_at = mapped_column(
        DateTime(timezone=True),
        server_default=text("(datetime('now'))"),
        server_onupdate=text("(datetime('now'))"),
    )


# TODO: extract to settings file
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
# TODO: setup echo=True logging only for non-prod
engine = create_engine(url=sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    Base.metadata.create_all(engine)


def get_db_session():
    with Session(engine) as session:
        yield session
