class Phone:  # parent
    def __init__(self, name, model, price):
        self.phone_name = name
        self.phone_model = model
        self.phone_price = price

    def phone_calling(self, phone_name):
        return f"phone calling.....{phone_name}"

    def model_fullname(self):
        return f"{self.phone_name}{self.phone_model}"


class Smartphone(Phone):  # child
    def __init__(self, name, model, price, rare_camera, ram, internal_memory):
        # Phone.__init__(self,name,model,price)
        super().__init__(name, model, price)
        # self.phone_name = name
        # self.phone_model = model
        # self.phone_price = price
        self.rare_camera = rare_camera
        self.internal_mem = internal_memory
        self.ram = ram

    # def phone_calling(self, phone_name):
    #     return f"phone calling.....{phone_name}"

    def __len__(self):
         return len(f"{self.phone_name}")
class khataraphone(Phone):  # child
    def __init__(self, name, model, price, rare_camera,front_camera,ram, internal_memory):
        Phone.__init__(self,name,model,price)
        self.rare_camera = rare_camera
        self.internal_mem = internal_memory
        self.ram = ram
        self.front_camera=front_camera
phone1 = Phone('nokia', '1100', "12000")
smartphone = Smartphone('samsung', '6x2', '16px', '4gbram', '32gb', "16000")
smartphone2 = khataraphone('oneplus', 'j7', '27000', '4gbram', '4mb','1500', "16000")

print(phone1.model_fullname())
print(smartphone.__len__())
print(smartphone.ram)
print(smartphone2.phone_name,smartphone2.front_camera)
# print(isinstance(smartphone2,Phone))
print(issubclass(smartphone,Smartphone))