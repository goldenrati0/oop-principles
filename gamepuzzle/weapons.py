class WeaponBehaviorInterface:
    def useWeapon(self) -> str:
        pass


class KnifeBehavior(WeaponBehaviorInterface):  # Knife IMPLEMENTS WeaponBehavior
    def useWeapon(self) -> str:
        return 'Cutting with knife'


class AxeBehavior(WeaponBehaviorInterface):  # Axe IMPLEMENTS WeaponBehavior
    def useWeapon(self) -> str:
        return 'Chopping with axe'


class BowAndArrowBehavior(WeaponBehaviorInterface):  # BowAndArrow IMPLEMENTS WeaponBehavior
    def useWeapon(self) -> str:
        return 'Throwing an arrow with a bow'


class SwordBehavior(WeaponBehaviorInterface):  # Sword IMPLEMENTS WeaponBehavior
    def useWeapon(self) -> str:
        return 'Swinging a sword'