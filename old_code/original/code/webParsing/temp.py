print("hello")

cars = ["Ford", "Volvo", "BMW"] 
#IndexError: list index out of range

try:
    print(cars[5])
except IndexError:
    print("no data")


if input < cars.size():
    print(cars[input])
else: 
    print("no data")