import turtle

paper = turtle.Screen()
pen = turtle.Turtle()

class shapes:
    def __init__(self):
        self.length = 0
        self.width = 0
        self.side = 0
        self.radius = 0
    
    def rectangle(self):
        self.length= int(input("Enter the length"))
        self.width = int(input("Enter the width"))
        pen.down()
        for i in range(2):
            pen.forward(self.length)
            pen.left(90)
            pen.forward(self.width)
            pen.left(90)
    
    def square(self):
        self.side = int(input("Enter the side length"))
        for i in range(4):
            pen.forward(self.side)
            pen.left(90)
    
    def circle(self):
        self.radius = int(input("Enter the radius"))
        pen.circle()

obj = shapes() 

shape = input("Enter the shape you want to draw\n1.Rectangle\n2.Square\n3.Circle")

if shape == "1":
    obj.rectangle()
elif shape == "2":
    obj.square()
elif shape == "3":
    obj.circle()
else:
    print("Enter a valid option")