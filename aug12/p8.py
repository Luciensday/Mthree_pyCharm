import os

os.chdir("test/sample1")
with open("file1.txt", "w") as f:
    f.write("Python files")

    