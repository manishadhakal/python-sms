# square=[]
# for i in range(1,11):
#   square.append(i**2)
# print(square)
#
#
# square2=[i**2 for i in range(1,11)]
# print(square2)
#
# negative=[]
# for i in range(1,10):
#     negative.append(-i)
#     print(negative)
#
#
# negative=[-i for i in range(1,11)]
# print(negative)



# find name
# name=['bhawana','sangita','manisha']
# name2=[]
# for i in name:
#     name2.append(i[0])
# print(name2)


# name3=[i[0] for i in name]
# print(name3)

# num=[1,2,3,4,5,6,7,8,9,10]
#
# num1=[i for i in range(1,21) if i%2==0]
# num2=[i for i in num if i%2!=0]
# print(num1)
# print(num2)


# list=[1,2,3,4,5,6]
# odd=[]
# for  i in num:
#     if i%2==0:
#         odd.append(i**2)
#     else:
#         odd.append(-i)
#print(odd)


# list=[1,2,3,4,5,6,7,8,9]
# odd=[i**2 if(i%2==0) else -i for i in num]
# print(odd)

list=[]
for i in  range(3):
    list.append([1,2,3])
print(list)

num1=[[i for i in range(1,4)] for i in range(3)]
print(num1)