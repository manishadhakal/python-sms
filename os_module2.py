import os,shutil
# print(os.getcwd())
# os.mkdir('manisha')
# os.mkdir(r'D:/movies3')
# open('manisha.txt','a').close()
# print(os.listdir())
# for item in os.listdir():
#     path=os.path.join(os.getcwd(),item)
#     print(path)

# for item in os.listdir(r'D:/'):
#     path=os.path.join(r'D:/',item)
#     print(path)
os.mkdir('new4')
shutil.copytree('new4','manisha/new')