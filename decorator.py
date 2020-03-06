#which enhance the functionality of thr function

def decorator_function(any__function):
    def warpper__function(*args,**kwargs):
        print("this is awesome")
        return any__function
    return warpper__function()
# this is awesome function
@decorator_function
def fun1(a):
    print(f"{a}this the first function")
decorator_function(fun1(1))
def fun2():
    print("this is the seond function")
# decorator_function(fun1())