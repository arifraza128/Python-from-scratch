import os

if os.path.exists("demo.txt"):
    os.remove("demo.txt")
    print("File deleted")
else:
    print("File not found")
