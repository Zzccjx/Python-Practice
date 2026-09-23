import re

with open("data.txt", "r") as file:
    text = file.read()

email = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

phone = re.findall(r"\b\d{10}\b", text)

age = re.findall(r"Age:\s*(\d+)", text)

print("Email:", email)
print("Phone:", phone)
print("Age:", age)
