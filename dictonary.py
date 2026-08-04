
student = {
    "name": "Nikunj",
    "age": 20,
    "city": "Rajkot"
}

print()
print(student)

print( student["name"])
print( student["age"])


student["age"] = 21


student["course"] = "MCA"

print("\nUpdated Dictionary:")
print(student)


print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Get Name:", student.get("name"))


print()

for key, value in student.items():
    print(key, ":", value)
