
def add(a, b):
    return a + b

print("Positional Arguments:")
print("Sum =", add(10, 20))



def student(name, age):
    print("Name:", name)
    print("Age:", age)

print("\nKeyword Arguments:")
student(age=22, name="Nikunj")



def greet(name="Student"):
    print("Hello", name)

print("\nDefault Arguments:")
greet()
greet("Nikunj")



def total(*numbers):
    return sum(numbers)

print("\nVariable-Length Arguments:")
print("Total =", total(10, 20, 30, 40))


def display_info(**details):
    for key, value in details.items():
        print(key, ":", value)

print("\nVariable-Length Keyword Arguments:")
display_info(name="Nikunj", age=22, city="Rajkot")
