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
    for i in range(2000000000):
        if i%2==0:
            i+=1

if __name__ == '__main__':
    run()

