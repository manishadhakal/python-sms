def is_even(a):
    return a%2==0
num=[1,2,3,4,5,6,7,8,9,10]
new_even=list(filter(is_even,num))
# new_even=list(filter(lambda a:a%2==0,num))
# print(new_even)

new_even=[a for a in new_even if a%2==0]
print(new_even)


