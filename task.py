# num1,num2,num3=input("enter the three number").split(" ")
# print(f"the number is :{int(num1)**2} ,{int(num2)**2} ,{int(num3)**2}") 1111


class Phone:
    def __init__(self,name,price,model):
        self.phone_name=name
        self.phone_price=price
        self.phone_model=model
    def phone_call(self,phone_name):
        return f" phone call.......... {phone_name}"
    def smartphone(self):
        return f"{self.phone_name}{self.phone_model}"
class Smartphone(Phone):
    def __init__(self,name,price,model,ram,camera):
        # Phone.__init__(self,name,price,model)
        super().__init__(name,price,model)
        # self.phone_name=name
        # self.phone_model=model
        # self.phone_price=price
        self.phone_camera=camera
        self.phone_ram=ram
    # def smartphone(self):
    #         return f"{self.phone_name}{self.phone_model}"
phone1=Phone('nokia','1100',1200)
smartphone1=Smartphone('samsung','e65we6','20000','60px','4gbram')
print(phone1.phone_price)
print(smartphone1.smartphone())



