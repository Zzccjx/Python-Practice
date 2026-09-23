#File 1: my_module.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

#File 2: main.py

import my_module

a = 10
b = 5

print("Addition:", my_module.add(a, b))
print("Subtraction:", my_module.subtract(a, b))
