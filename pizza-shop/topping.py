from item import Item
from free_item import FreeItem


class Topping(Item):  # IS-A Item
    def __init__(self) -> None:
        super().__init__()


class CheddarCheese(Topping):  # IS-A Topping
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Cheddar Cheese')
        self.set_price(0.2)


class FreeCheddarCheese(CheddarCheese, FreeItem):  # IS-A CheddarCheese, IS-A FreeItem
    def __init__(self) -> None:
        super().__init__()

    def update_item_price(self):
        self.set_price(0.0)

    def remove_additional_free_items(self) -> None:
        self.clear_free_items()


class MozarellaCheese(Topping):  # IS-A Topping
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Mozarella Cheese')
        self.set_price(0.2)


class Pepperoni(Topping):  # IS-A Topping
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Pepperoni')
        self.set_price(0.3)


class FreePepperoni(Pepperoni, FreeItem):  # IS-A Pepperoni, IS-A FreeItem
    def __init__(self) -> None:
        super().__init__()

    def update_item_price(self):
        self.set_price(0.0)

    def remove_additional_free_items(self) -> None:
        self.clear_free_items()


class Bacon(Topping):  # IS-A Topping
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Bacon')
        self.set_price(0.5)


class BaconWithFreeItems(Bacon):  # IS-A Bacon
    """
    Created this class just to make things simpler.
    BaconWithFreeItems might look unnecessary becuase Item HAS-A FreeItem, so could have
    added those FreeItem(s) in Bacon class. In that case, we needed to add a bool in the
    constructor should_add_free_items. I did not want to add this bool variable, and hence
    the new class.
    """
    def __init__(self) -> None:
        super().__init__()

        self.add_free_item(FreeCheddarCheese())


class BlackOlive(Topping):  # IS-A Topping
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Black Olive')
        self.set_price(0.3)
