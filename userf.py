
def add(a, b):
    print("Addition =", a + b)

def student(name, age):
    print("Name :", name)
    print("Age  :", age)

def country(name="India"):
    print("Country :", name)

def total_marks(*marks):
    print("Total Marks =", sum(marks))


print("Positional Argument")
add(10, 20)

print("\nKeyword Argument")
student(age=20, name="Nikunj")

print("\nDefault Argument")
country()
country("Canada")

print("\nVariable-Length Argument")
total_marks(70, 80, 90)
total_marks(50, 60)
