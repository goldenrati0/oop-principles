from item import Item
from topping import FreePepperoni


class PizzaCrust(Item):  # IS-A Item
    def __init__(self) -> None:
        super().__init__()


class ThinCrust(PizzaCrust):  # IS-A Crust
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Thin')
        self.set_price(2.0)


class ThickCrust(PizzaCrust):  # IS-A Crust
    def __init__(self) -> None:
        super().__init__()

        self.set_name('Thick')
        self.set_price(3.0)


class ThickCrustWithFreeItems(ThickCrust):  # IS-A ThickCrust
    """
    Created this class just to make things simpler.
    ThickCrustWithFreeItems might look unnecessary becuase Item HAS-A FreeItem, so could have
    added those FreeItem(s) in ThickCrust class. In that case, we needed to add a bool in the
    constructor should_add_free_items. I did not want to add this bool variable, and hence
    the new class.
    """
    def __init__(self) -> None:
        super().__init__()

        self.add_free_item(FreePepperoni())
