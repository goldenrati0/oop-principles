from characters import Character, King, Queen, Knight, Troll
from weapons import KnifeBehavior, BowAndArrowBehavior, AxeBehavior, SwordBehavior

king: Character = King()
king.setWeapon(AxeBehavior())

queen: Character = Queen()
queen.setWeapon(KnifeBehavior())

knight: Character = Knight()
knight.setWeapon(SwordBehavior())

troll: Character = Troll()
troll.setWeapon(BowAndArrowBehavior())

if __name__ == '__main__':
    king.fight()
    queen.fight()
    knight.fight()
    troll.fight()

