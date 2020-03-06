while True:
    try:
        number=int(input("enter your number"))
    except ValueError:
        print("please take valid input")
    except:
        print("unexpected error")
    else:
        print(f"this is the enter number{number}")
        break
    finally:
        print("this is finally for program")