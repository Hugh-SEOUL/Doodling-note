class Circle:
    def __init__(self,radius = 0):
        self.radius = radius
    def __eq__(self, oter):
        return self.radius == oter.radius
    
if __name__ == "__main__":
    circle1 = Circle(10)
    circle2 = Circle(10)
    if circle1 == circle2:
        print("같다")