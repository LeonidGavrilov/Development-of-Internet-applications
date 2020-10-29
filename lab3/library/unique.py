from library.gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_elements = set()
        self.case = False
        for key in kwargs:
            if key is "ignore_case":
                if kwargs[key] is True:
                    self.case = True
        self.data = iter(items)

    def __next__(self):
        while True:
            current = self.data.__next__()
            if self.case is True and type(current) is str:
                new_item = current.lower()
            else:
                new_item = current
            if new_item not in self.used_elements:
                self.used_elements.add(new_item)
                return new_item

    def __iter__(self):
        return self