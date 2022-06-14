def add(*args):
    s = 0
    for n in args:
        s += n

    return s

res = add(1, 2, 3, 4, 5, 32)
print(res)

def calculate(n, **kwargs):
    # for key, values in kwargs.items():
        # print(key)
        # print(values)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=4)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seat = kw.get("seats")

my_car = Car(make="Nissen", model="GT-R", color="red")
print(my_car.make)
print(my_car.model)
print(my_car.color)