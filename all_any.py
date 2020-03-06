number1=[1,2,3,4,5,6,7,8,9]
number2=[1,3,9,5,9,6]
# for num in number1:
#     if num%2==0:
#         print(True)
#  print(all(number1))
# print(all(True,False,True,True))

print(any([num%2==0 for num in number2]))