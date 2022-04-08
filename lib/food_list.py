import sys, os
sys.path.append(os.path.join(sys.path[0],'objects'))

from chinelao import Chinelao
from lagarto import Lagarto
from costelinha import Costelinha
from frango_assado import Frango_Assado

FOOD_LIST = [
    Costelinha,
    Frango_Assado,
    Chinelao,
    Lagarto,
]