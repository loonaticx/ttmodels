import os
os.chdir("../")

makefile = "Makefile"

for root, _, files in os.walk("."):
    for file in files:
        if not file.startswith(makefile):
            continue
        file = os.path.join(root, file)
        print("Removing " + str(file))
        os.remove(file)