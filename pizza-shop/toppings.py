from typing import List

from free_item import FreeItemInterface
from item import ItemInterface


class ToppingsInterface(ItemInterface):  # IS-A Item
    def __init__(self) -> None:
        super().__init__()


class CheddarCheese(ToppingsInterface):  # IS-A Topping
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Cheddar Cheese')
        self.set_price(0.2)


class MozarellaCheese(ToppingsInterface):  # IS-A Topping
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Mozarella Cheese')
        self.set_price(0.2)


class Pepperoni(ToppingsInterface):  # IS-A Topping
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Pepperoni')
        self.set_price(0.3)


class Bacon(ToppingsInterface):  # IS-A Topping
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Bacon')
        self.set_price(0.5)

        self.add_free_item(FreeItemInterface(CheddarCheese()))
