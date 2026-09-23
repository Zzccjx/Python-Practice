import os
import sys

print("Current Directory:")
print(os.getcwd())

folder = "MyFolder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Directory created.")
else:
    print("Directory already exists.")

print("\nFiles and Folders:")
print(os.listdir())

print("\nPython Version:")
print(sys.version)
