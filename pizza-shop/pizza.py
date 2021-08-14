from abc import ABC, abstractmethod
from typing import List

from item import Item
from crust import PizzaCrust, ThinCrust
from topping import Topping, MozarellaCheese, BlackOlive


class Pizza(Item, ABC):  # IS-A Item
    def __init__(self) -> None:
        super().__init__()

        self.set_price(0.2)  # base price

        self.crust: PizzaCrust = None  # HAS-A PizzaCrust
        self.toppings: List[Topping] = []  # HAS-A Topping

        self.add_primary_crust()
        self.add_primary_topping()

    @abstractmethod
    def add_primary_topping(self):
        raise NotImplementedError

    @abstractmethod
    def add_primary_crust(self):
        raise NotImplementedError

    def add_to_price(self, amount: int) -> None:
        self.price += amount

    def add_free_items(self, item: Item) -> None:
        for free_item in item.get_free_items():
            self.add_free_item(free_item)

    def set_crust(self, crust: PizzaCrust) -> None:
        if self.crust:
            self.set_price(self.get_price() - self.crust.get_price())  # deduct old crust price

        self.crust = crust
        self.set_price(self.price + self.crust.get_price())  # add new crust price

        self.add_free_items(crust)

    def add_topping(self, topping: Topping) -> None:
        self.toppings.append(topping)

        self.set_price(self.price + topping.get_price())

        self.add_free_items(topping)

    def get_details(self) -> None:
        print('=' * 25)

        print(f'{self.name} Pizza')
        print(f'Crust: {self.crust.get_name()}')

        if self.toppings:
            topping_names = ', '.join([topping.get_name() for topping in self.toppings])
            print(f'Toppings: {topping_names}')

        if self.get_free_items():
            free_item_names = ', '.join([free_item.get_name() for free_item in self.get_free_items()])
            print(f'Free items: {free_item_names}')

        print(f'Total price: ${self.get_price()}')

        print('=' * 25)


class Margherita(Pizza):  # IS-A Pizza
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Margherita')

    def add_primary_crust(self):
        self.set_crust(ThinCrust())

    def add_primary_topping(self):
        self.add_topping(MozarellaCheese())


class BBQChicken(Pizza):  # IS-A Pizza
    def __init__(self) -> None:
        super().__init__()

        self.set_name('BBQ Chicken')

    def add_primary_crust(self):
        self.set_crust(ThinCrust())

    def add_primary_topping(self):
        self.add_topping(BlackOlive())
