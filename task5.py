# name=['manisha','cristina','manish']
# def function(l,target):
#     for position,names in  enumerate(l):
#         if names==target:
#             return position
#     return -1
# print(function(name,'cristina'))


num=[1,2,3,4,5]
def power(a):
    return a**2
# new_power=list(map(power,num))
new_power=list(map(lambda a:a**2,num))
print(new_power)
