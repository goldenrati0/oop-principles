from crust import ThickCrustWithFreeItems
from topping import Bacon, Pepperoni, BaconWithFreeItems
from pizza import Pizza, Margherita, BBQChicken


margerita: Pizza = Margherita()
margerita.add_topping(BaconWithFreeItems())
margerita.get_details()

bbq: Pizza = BBQChicken()
bbq.set_crust(ThickCrustWithFreeItems())
bbq.add_topping(Bacon())
bbq.add_topping(Pepperoni())
bbq.get_details()
