# def function(name,*args,lastname='unknown',**kwargs):
#     print(name)
#     print(args)
#     print(lastname)
#     print(kwargs)
# function('manisha',1,2,3,4,5,lastname='dhakal',firstname='siyona',lname='chettri')

# def function(**kwargs):
#   for i in kwargs.items():
#        print(i)
# name={'name1':'manisha dhakal','age':'20'}
# function(**name)

def function(*args):
    multiply=1
    for i in args:
        multiply*=i
    return multiply
print(function(1,2,3,4))