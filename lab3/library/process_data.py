import json
from library.unique import Unique
from library.print_result import print_result
from library.cm_timer import cm_time_1
from library.field import field
from library.gen_random import gen_random
import sys
# Сделаем другие необходимые импорт

path = "library/data_light.json"

with open(path, encoding="UTF-8") as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return sorted(list(Unique(field(arg, 'job-name'), ignore_case=True)), key=lambda x: str.casefold(x))


@print_result
def f2(arg):
    return list(filter(lambda x: "программист" in x.lower(), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    return dict((zip(arg, gen_random(len(arg), 100000, 200000))))
