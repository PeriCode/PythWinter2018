# import random, math, time
import random # подключаем целиком весь модуль
from random import randint # подключаем конкретную функцию из модуля
from math import sqrt as r_sqrt # даем имя импортируемой функции
from cmath import sqrt as c_sqrt
# import my_module # подключили собственный модуль
from my_module import inc, dec
# import time
from time import * # тоже импортируем всю библиотеку

# print(q(4))
# print(r_sqrt(256))
print(inc(5))
sleep(3)
print(dec(5))