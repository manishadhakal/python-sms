wining_number=27
user_nameinput=input("enter your guess number")
user_input=int(user_nameinput)
if wining_number==user_input:
     print("you win!!!!!")
else:

    if user_input>wining_number:
      print("you are  high")
    if user_input<wining_number:
       print("you are low")
