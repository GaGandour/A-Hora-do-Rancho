import sys, os
sys.path.append(os.path.join(sys.path[0],'objects'))

from chinelao import Chinelao
from lagarto import Lagarto
from costelinha import Costelinha
from frango_assado import Frango_Assado

FOOD_LIST = [
    (Costelinha.food_name, Costelinha),
    (Frango_Assado.food_name, Frango_Assado),
    (Chinelao.food_name, Chinelao),
    (Lagarto.food_name, Lagarto),
]