# fromkeys
# more_info=dict.fromkeys(('name','age','class'),'unkown')
# more_info=dict.fromkeys(('abc'),'unkown')
# print(more_info)

# get method\
user_info={
    'name':'manisha',
    'age':20,
    'gender':'female',
    'fav_movie':['son of satyamurti2','allu arjun,nitin']
}
# get method
# print(user_info['names']) error keyerror
# print(user_info.get('names')) value access and show none
# print(user_info.get('fav','not found!!')) to show message error

# clear method
# user_info.clear()
# print(user_info)

# sagar=user_info.copy()
# print(sagar)