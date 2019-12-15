from ctypes import *
from datetime import datetime

def timeit(func):
    def wrapper():
        start = datetime.now()
        result=func()
        end = datetime.now()
        print(end - start)
        return result
    return wrapper

@timeit
def run():
    adder = CDLL('/home/wb_69/PycharmProjects/ctypes/add.so')
    res_int = adder.add_int()


if __name__ == '__main__':
    run()
