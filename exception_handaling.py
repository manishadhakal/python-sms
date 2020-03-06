while True:
 try:
     age = int(input("enter a age"))
     if age<= 18:
         print("you cannot watch movie")
     else:
         print('you can watch this movie')
         break



 except ValueError:
    print("pleasase enter valid value ")
 except:
     print("invailid input plese try it")

