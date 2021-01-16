import os
os.chdir("../")

egg = ".egg"

for root, _, files in os.walk("."):
    for file in files:
        if not file.endswith(egg):
            continue
        file = os.path.join(root, file)
        print("Removing " + str(file))
        os.remove(file)