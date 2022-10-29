import inspect
import random
import sys

data = "string"

class Human:
    pass

def data2():
    pass


data = data2
print(inspect.ismodule(random))
print(inspect.isclass(Human))
print(inspect.isfunction(Human))

print(sys.executable)

for met in dir(random):
    print(met)
