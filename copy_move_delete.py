import shutil
import os

with open("source.txt", "w") as file:
    file.write("Hello Python")

shutil.copy("source.txt", "copy.txt")
print("File copied.")

shutil.move("copy.txt", "moved.txt")
print("File moved.")

if os.path.exists("moved.txt"):
    os.remove("moved.txt")
    print("File deleted.")
