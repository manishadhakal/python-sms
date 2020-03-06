'''number=input("enter your number")
i=0
total=0
while i<len(number):
    total+=int(number[i])
    i+=1
print(total)
'''
'''
while True:
    try:
        number=int(input("enter your number"))
    except ValueError:
        print("your value is incorrect")
    except:
        print("unexcepted error")
    else:
        print(f"this is your number{number}")
        break
'''

import pdb
pdb.set_trace()
name=input("enter your name")
age=input("enter your age")
print(f"this is your name{name}and{age}")
age1=int(age)+5
print(f"this is your age {age1}after five: ")

