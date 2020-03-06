'''
write a python program to find those numbers which is divisbile
by 7 abd multiple of 5, between 1500 and 2700 (both included)
'''
number=[]
for i in range(1700,1500):
    number.append(i/7)
    number.append(i*5)
print(number)



#write a python program to construct the following pattern,using a nested
#for loop(
'''n=5
for i in range(0,n+1):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n,0,-1):
    for j in range(i-1):
        print("*",end=" ")
    print()
'''


'''write a python program to guess a number between 1 to 9 go to 
the editors 
#note: user is prompted to enter a guess.
#if the user guesses wrong then the prompt appers again until the guess 
is correct on the sucessful guess
user will get a well guessed "message",the program will exit'''
'''import random
guess_number=random.randint(1,9)
number=int(input("enter your guess number"))
guess=1
message_pass=False
while not message_pass:
    if guess_number==number:
        print(f"well guessed??guess the number{guess}times")
        message_pass=True
    else:
        if number<guess_number:
            print("you are right")
            guess+=1
            number=int(input("guess again:"))
        if number < guess_number:
                print("you are wrong")
                guess += 1
                number=int(input("guess again:"))'''


'''
wite a python program to convert temperatures to and from celsius,
fahrenheit.go to the editors 
'''
'''
def celcius():
    celcius=int(input("enter the temperature in celcius:"))
    fahrenheit=(celcius*1.8)+32
print("temperature in fahrenheit is :")
def fahrenheit():
    temperature = int(int("enter the celcius in temperature:"))
    celcius=(fahrenheit-32)*5/9
    celcius=fahrenheit()*5/9
    print("celcius in fahrenheit is:")
'''
