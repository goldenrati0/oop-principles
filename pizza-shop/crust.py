from typing import List

from item import ItemInterface
from free_item import FreeItemInterface
from toppings import Pepperoni


class PizzaCrustInterface(ItemInterface):  # IS-A Item
    def __init__(self) -> None:
        super().__init__()


class ThinCrust(PizzaCrustInterface):  # IS-A Crust
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Thin')
        self.set_price(2.0)


class ThickCrust(PizzaCrustInterface):  # IS-A Crust
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Thick')
        self.set_price(3.0)

        self.add_free_item(FreeItemInterface(Pepperoni()))
