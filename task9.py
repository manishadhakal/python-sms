class Parameter:
    def __init__(self,length,width):
        self.length1=length
        self.width1=width
    def rectangular(self):
        return 2*(self.length1+self.width1)
circle1=Parameter(5,8)
print(circle1.rectangular())





