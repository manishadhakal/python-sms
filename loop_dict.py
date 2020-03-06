user_info={
    'name':'sagar',
    'age':24,
    'gender':'male',
    'fav_movie':['war','salman khan']
}

# for i in user_info.values():
#     print(i)

# if 'sagar' in user_info.values():
#     print("present")
# else:
#     print("not present")
#

# user_info_keys=user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

# user_info_values=user_info.values()
# print(user_info_values)
# print(type(user_info_values))


# user_info_items=user_info.items()
# print(user_info_items)
# print(type(user_info_items))
# [('name', 'sagar'), ('age', 24), ('gender', 'male'), ('fav_movie',
# ['war', 'salman khan'])])

for keys,values in user_info.items():
    print(f" keys are {keys} and values are {values}")


