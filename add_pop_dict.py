# user_info={
#     'name':'sagar',
#     'age':24,
#     'gender':'male',
#     'fav_movie':['war','salman khan']
# }

# add data to list in dictinores
# user_info['fav_song']=['song1','song2']
# print(user_info)
#user_info['fav_song']=['song1','song2']
# print(user_info)

# poped_items=user_info.pop('name')
# print(f"ppoped item is{poped_items} ")
# print(user_info)
# bhawana=user_info.popitem()
# print(bhawana)
# print(user_info)


user_info={
    'name':'manisha',
    'age':20,
    'gender':'female',
    'fav_movie':['son of satyamurti2','allu arjun,nitin']
}
for i in user_info.values():
     print(i)
if 'manisha' in user_info.values():
     print("present")
else:
     print("not present")