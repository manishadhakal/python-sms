list=[1,2,3,4]
def function(*args):
    if all([(type(arg)==int or type(arg)== float) for arg in args]):
        sum=0
        for i in args:
            sum+=i
        return sum
    return "wrong input"
print(function(*list))
