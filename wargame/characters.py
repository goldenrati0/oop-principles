from abc import ABC

from weapons import WeaponBehaviorInterface


class Character(ABC):

    def __init__(self) -> None:
        self.name = None
        self.weapon = WeaponBehaviorInterface()  # Character HAS-A WeaponBehavior

    def setName(self, name):
        self.name = name

    def setWeapon(self, weapon: WeaponBehaviorInterface):
        self.weapon = weapon

    def fight(self) -> None:
        print(f'{self.name} is {self.weapon.useWeapon()}')


class King(Character):  # King IS-A Character

    def __init__(self) -> None:
        super().__init__()
        self.setName('King')


class Queen(Character):  # Queen IS-A Character

    def __init__(self) -> None:
        super().__init__()
        self.setName('Queen')


class Knight(Character):  # Knight IS-A Character

    def __init__(self) -> None:
        super().__init__()
        self.setName('Knight')


class Troll(Character):  # Troll IS-A Character

    def __init__(self) -> None:
        super().__init__()
        self.setName('Troll')
