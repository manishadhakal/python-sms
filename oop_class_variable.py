class Circle:
    pie=3.14
    def __init__(self,radius):
        # self.pi=pi
        self.radius=radius
    def circumtance(self):
        return 2*Circle.pie*self.radius
circle1=Circle(5)
circle2=Circle(6)
print(circle1.circumtance())
print(circle2.circumtance())




