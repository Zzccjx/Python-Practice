import re

text = "Python is easy. Python is powerful."

result = re.match(r"Python", text)

if result:
    print("match():", result.group())

result = re.search(r"powerful", text)

if result:
    print("search():", result.group())

result = re.findall(r"Python", text)

print("findall():", result)
