# with open('file.txt','a') as f:
#     data=f.write('my name is manisha dhakal from bhairahawa')
#     print(data)
#
# with open('file.txt','r+') as f:
#     f.seek(len(f.read()))
#     f.write('this is hub it')

with open('file.txt','r') as rf:
    with open('file1.txt','w') as wf:
        wf.write(rf.read())


