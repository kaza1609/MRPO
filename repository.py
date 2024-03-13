import abc
from abc import ABC, abstractmethod
from models import *


class AbstractRepository(ABC):

    @abstractmethod
    def save_item(self, item):
        pass

    @abstractmethod
    def get_item(self, index):
        pass


class EventRepository(AbstractRepository):
    __storage = []

    def save_item(self, item: Event):
        self.__storage.append(item)
        return item

    def get_item(self, index: int):
        return self.__storage[index]


class PersonRepository(AbstractRepository):
    __storage = []

    def save_item(self, item: Person):
        self.__storage.append(item)
        return item

    def get_item(self, index: int):
        return self.__storage[index]


class PositiveEmotionsRepository(AbstractRepository):
    __storage = []

    def save_item(self, item: PositiveEmotions):
        self.__storage.append(item)
        return item

    def get_item(self, index: int):
        return self.__storage[index]


class NegativeEmotionsRepository(AbstractRepository):
    __storage = []

    def save_item(self, item: NegativeEmotions):
        self.__storage.append(item)
        return item

    def get_item(self, index: int):
        return self.__storage[index]


class PositiveThoughtRepository(AbstractRepository):
    __storage = []

    def save_item(self, item: PositiveThought):
        self.__storage.append(item)
        return item

    def get_item(self, index: int):
        return self.__storage[index]


class NegativeThoughtRepository(AbstractRepository):
    __storage = []

    def save_item(self, item: NegativeThought):
        self.__storage.append(item)
        return item

    def get_item(self, index: int):
        return self.__storage[index]


class CalmingTechniqueRepository(AbstractRepository):
    __storage = []

    def save_item(self, item: CalmingTechnique):
        self.__storage.append(item)
        return item

    def get_item(self, index: int):
        return self.__storage[index]
