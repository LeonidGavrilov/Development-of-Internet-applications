import time
from contextlib import contextmanager

class cm_time_1:
    def __enter__(self):
        self.time = time.time()

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print(time.time() - self.time)

@contextmanager
def cm_time_2():
    timer = time.time()
    yield
    print(time.time() - timer)
