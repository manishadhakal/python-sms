num=[1,2,3,4,5,6,7]
def power(a):
    return a**2
#  new_power=list(map(power,num))
# new_power=list(map(lambda a:a**2,num))
# print(new_power)

new_power1=[a**2 for a in num]
print(new_power1)
