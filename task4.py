# def cube_find(num):
#     cube={}
#     for i in range(1,num):
#         cube[i]=i**3
#     return cube
# print(cube_find(8))


#task5
user={}
name=input("what is your name : ")
age=input("what is your age : ")
gender=input("what is your gender : ")
fav_movie=input("what are your fav movie : ").split(",")
fav_song=input("what are your fav song : ").split(",")

user['name']=name
user['age']=age
user['gender']=gender
user['fav_movie']=fav_movie
user['fav_song']=fav_song

# print(user) simlple  print
for keys,values in user.items():
    print(f"{keys}:{values}")