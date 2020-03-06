# def function(a,b):
#     return a+b
#  print(function(1,2))
#
#
# def function(*args):
#     multiply=1
#     for i in args:
#         multiply*=i
#     return multiply
# num=[1,2,3,4,5,6]
# print(function(*num))



# def function(**kwargs):
#     print(kwargs)
# function(firstname='manisha',lastame='dhakal',age='20')


# def function(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
# function(name='manisha',last='dhakal',age='20')


# def function(**kwargs):
#
#     for i in kwargs.items():
#         print(i)
# name={'name1':'manisha dhakal','age':'20')
# function(**name)


def function(**kwargs):
    addition=1
    for i in kwargs:
       addition+=i
       print(i)
addition={"1:2","2:3"}
function(addition)