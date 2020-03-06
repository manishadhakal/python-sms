name=input("enter your name")
for i in range(len(name)):
    print(f"{name[i]}:{name.count(name[i])}")
