from abc import ABC, abstractmethod

from item import Item

class FreeItem(Item, ABC):  # IS-A Item
    def __init__(self) -> None:
        super().__init__()

        self.update_item_price()  # because it is free
        self.remove_additional_free_items()  # free-items cannot have more free items

    @abstractmethod
    def update_item_price(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_additional_free_items(self) -> None:
        raise NotImplementedError

    def add_free_item(self, item: 'FreeItem') -> None:
        raise Exception('Free item cannot have free items')
