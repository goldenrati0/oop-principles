from abc import ABC
from typing import List

from item import ItemInterface
from crust import PizzaCrustInterface
from toppings import ToppingsInterface


class Pizza(ItemInterface, ABC):  # IS-A Item
    def __init__(self) -> None:
        super().__init__()

        self.set_price(0.2)  # base price

        self.crust: PizzaCrustInterface = None  # HAS-A PizzaCrust
        self.toppings: List[ToppingsInterface] = []  # HAS-A Toppings

    def add_free_items(self, item: ItemInterface) -> None:
        for free_item in item.get_free_items():
            super().add_free_item(free_item)

    def set_crust(self, crust: PizzaCrustInterface) -> None:
        self.crust = crust
        self.set_price(self.price + self.crust.get_price())

        self.add_free_items(crust)

    def add_topping(self, topping: ToppingsInterface) -> None:
        self.toppings.append(topping)
        self.set_price(self.price + topping.get_price())

        self.add_free_items(topping)

    def bake(self) -> None:
        print('=' * 25)

        print(f'Baking {self.name} Pizza')
        print(f'Crust: {self.crust.get_name()}')

        if self.toppings:
            topping_names = ', '.join([topping.get_name() for topping in self.toppings])
            print(f'Toppings: {topping_names}')

        if self.get_free_items():
            free_item_names = ', '.join([free_item.get_name() for free_item in self.get_free_items()])
            print(f'Free items: {free_item_names}')

        print(f'Total price: {self.get_price()}')

        print('=' * 25)


class Margherita(Pizza):  # IS-A Pizza
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Margherita')


class BBQChicken(Pizza):  # IS-A Pizza
    def __init__(self) -> None:
        super().__init__()

        self.set_name('BBQ Chicken')

