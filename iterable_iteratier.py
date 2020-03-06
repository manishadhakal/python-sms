num=[1,2,3,4,5,6,7]  #list ,string,tuple
def power(a):
    return a**2
num2=map(lambda a:a**2,num)  #fun,filter,map
new_iter=iter(num)
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))


print(next(num2))
print(next(num))

for i in num2:
    print(i)
for j in num2:
    print(j)