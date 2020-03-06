class tap:
    def __init__(self,name,model_number,price):
        self.name1=name
        self.model2=model_number
        self.price2=price
        # self.model_fullname=name+" "+model_number
    def model_fullname(self):
        return f"{self.model2} {self.name1}"
labtop1=tap('dell','xxxx10hpxx',70000)
labtop2=tap('dell','xxxx10hpxx',70000)
# print(labtop1.name1,labtop1.model2,labtop1.price2)
# print(labtop2.name1,labtop2.model2,labtop2.price2)
print(labtop2.name1,labtop2.model2,labtop2.price2)