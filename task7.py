
def decorator_function(any__function):
    def warpper__function(*args,**kwargs):
        # print("this is awesome")
        return any__function
    return warpper__function()
@decorator_function
def fun1(a):
    print(f"{a}this the first function")
decorator_function(fun1(1))
def fun2():
    print("this is the seond function")












@decorator_function
def fun1(num1,num2,num3):
    print(f"this is your average:{int(num1)+int(num2)+int(num3)//3}")
decorator_function(fun1(1,2,3))
def fun2():
    print("this is the seond function")
