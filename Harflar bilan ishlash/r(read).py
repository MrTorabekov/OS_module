# file read

with open("matn1.txt", "r") as file:
    data = file.read()
    for i in data.split(" "):
        if "a" in i:
            print(i)
        else:
            continue
