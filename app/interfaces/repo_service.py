from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class RepoService(ABC, Generic[T]):
    @abstractmethod
    def create(self, entity: T) -> T:
        pass

    # @abstractmethod
    # def get_by_id(self, id: int) -> T | None:
    #     pass

    @abstractmethod
    def get_all(self) -> list[T]:
        pass

    # @abstractmethod
    # def update(self, entity: T) -> T:
    #     pass

    # @abstractmethod
    # def delete(self, id: int) -> None:
    #     pass
