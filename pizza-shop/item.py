from abc import ABC
from typing import List


class ItemInterface(ABC):

    def __init__(self) -> None:
        self.name: str = None
        self.price: float = None

        from free_item import FreeItemInterface

        self.free_items: List[FreeItemInterface] = []  # HAS-A FreeItem

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_price(self, price: float):
        self.price = price

    def get_price(self) -> float:
        return self.price

    def add_free_item(self, item: 'FreeItemInterface') -> None:
        self.free_items.append(item)

    def clear_free_items(self) -> None:
        while self.free_items:
            self.free_items.pop()  # in-place mutation

    def get_free_items(self) -> List['FreeItemInterface']:
        return self.free_items
