name=input("enter your name")
i=0
while i< len(name):
    print(f"{name[i]}:{name.count(name[i])}")
    i+=1