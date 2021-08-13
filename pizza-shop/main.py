from crust import ThinCrust, ThickCrust
from toppings import MozarellaCheese, Bacon, Pepperoni
from pizza import Margherita, BBQChicken


margerita = Margherita()
margerita.set_crust(ThinCrust())
margerita.add_topping(MozarellaCheese())
margerita.bake()

bbq = BBQChicken()
bbq.set_crust(ThickCrust())
bbq.add_topping(Bacon())
bbq.add_topping(Pepperoni())
bbq.bake()
