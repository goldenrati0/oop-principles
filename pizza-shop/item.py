from abc import ABC
from typing import List


class Item(ABC):

    def __init__(self) -> None:
        self.name: str = None
        self.price: float = None

        from free_item import FreeItem

        self.free_items: List[FreeItem] = []  # HAS-A FreeItem

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_price(self, price: float):
        self.price = price

    def get_price(self) -> float:
        return self.price

    def add_free_item(self, item: 'FreeItem') -> None:
        self.free_items.append(item)

    def clear_free_items(self) -> None:
        while self.free_items:
            self.free_items.pop()  # in-place mutation

    def get_free_items(self) -> List['FreeItem']:
        return self.free_items
