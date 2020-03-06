
def func(*args):
    multiply = 1
    for i in args:
        multiply*=i
    return multiply
num=[2,7,3,4,5,6]
print(func(*num))
