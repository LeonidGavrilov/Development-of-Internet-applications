from library.unique import *
from library.gen_random import gen_random

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
# data = gen_random(6, 3, 10)
for i in Unique(data, ignore_case=True):
    print(i)

