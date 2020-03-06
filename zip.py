# user=['user1','user2','user3']
# username=['manisha','cristial','shyam']
# lastname=['dhakal','thapa','chettri']
# print(list(zip(user,username,lastname)))



# # zip function with loop

# l1=[1,3,5,7]
# l2=[2,4,6,8]
l=[(1,2),(3,4),(5,6),(7,8)]
print(list(zip(*l)))

l1,l2=zip(*l)
print(list(l1))
print(list(l2))



# new_list=[]
# for pair in zip(l1,l2):
#     new_list.append(max(pair))
# print(new_list)