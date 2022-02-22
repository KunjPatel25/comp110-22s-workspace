from turtle import Turtle, colormode, done
colormode(255)

cc: Turtle = Turtle()

cc.begin_fill()
cc.speed(1000)
cc.pencolor("black")
i: int = 0
while i < 180:
    cc.forward(2)
    cc.left(1)
    i = i + 1
cc.end_fill
done()


rectangle: Turtle = Turtle()

rectangle.forward(50)
rectangle.left(90)
rectangle.forward(75)
rectangle.left(90)
rectangle.forward(50)
rectangle.left(90)
rectangle.forward(75)
rectangle.left(90)


leo: Turtle = Turtle()

leo.penup()
leo.goto(-300, 300)
leo.pendown()

leo.begin_fill()
leo.speed(50)
leo.color("blue", "red")
i: int = 0
while i < 3:
    leo.forward(500)
    leo.left(120)
    i = i + 1
leo.end_fill()


bob: Turtle = Turtle()

bob.penup()
bob.goto(-300, -300)
bob.pendown()

bob.begin_fill()
bob.speed(100)
bob.color("black", "blue")
side_length: float = 500
i: int = 0
while i < 3: 
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
bob.end_fill()


a_turtle: Turtle = Turtle()

a_turtle.penup()
a_turtle.goto(-200, -300)
a_turtle.setheading(0.0)
a_turtle.pendown()

a_turtle.forward(400)
a_turtle.left(90)
a_turtle.forward(600)
a_turtle.left(90)
a_turtle.forward(400)
a_turtle.left(90)
a_turtle.forward(600)
a_turtle.left(90)
done()

cc: Turtle = Turtle()

cc.begin_fill()
cc.speed(1000)
cc.pencolor("black")
i: int = 0
while i < 360:
    cc.forward(3)
    cc.left(1)
    i = i + 1
cc.end_fill