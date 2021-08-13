from item import ItemInterface


class FreeItemInterface(ItemInterface):  # IS-A Item
    def __init__(self, item: ItemInterface) -> None:
        super().__init__()
        self.item = item

        self.item.set_price(0.0)  # because it is free
        self.item.clear_free_items()  # free-items cannot have more free items

    def get_name(self) -> str:  # Override because Item is wrapped in FreeItem
        return self.item.get_name()
