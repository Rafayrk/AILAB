class Shape:

   @staticmethod
   def printtype(self):
    print("Type")



    def draw(self):
     print("draw")

    def area(self):
     print("Area")




class Rectangle(Shape):

    length=0;

    width=0;

    def draw(self):

        print("Rectangle draw")

    def area(self):
        print("Rectangle Area")


class Triangle(Shape):



    b = 0;

    c=0;

    def __init__(self):
        self.a=0
        print("co")


    def draw(self):

        print("Triangle draw")

    def area(selfs):
        print("Triangle Area")

tri=Triangle()
tri.draw()