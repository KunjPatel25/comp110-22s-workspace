"""This is a drawing of a basketball court because basketball is one of my favorite hobbies and is something I really enjoy."""

__author__ = "730477806"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scence."""
    ertle: Turtle = Turtle()
    draw_court(ertle, -200, -300, 400, 600)
    draw_paint(ertle, -50, -300, 100, 150)
    draw_paint_two(ertle, -50, 300, 100, 150)
    draw_three_point_line(ertle, 175, -300, 350)
    draw_three_point_line_two(ertle, -175, 300, 350)
    draw_center_circle(ertle, 0, 50, 40)
    draw_basketball(ertle, -25, 15, 10)
    draw_basketball(ertle, 25, 15, 10)
    done()


def draw_court(a_turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draw a large rectangle whose bottom left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    a_turtle.begin_fill()
    a_turtle.speed(0)
    a_turtle.pencolor("black")
    a_turtle.fillcolor(251, 238, 172)
    a_turtle.forward(width)
    a_turtle.left(90)
    a_turtle.forward(length)
    a_turtle.left(90)
    a_turtle.forward(width)
    a_turtle.left(90)
    a_turtle.forward(length)
    a_turtle.left(90)
    a_turtle.end_fill()

    a_turtle.penup()
    a_turtle.goto(-200, 0)
    a_turtle.pendown()
    a_turtle.goto(200, 0)


def draw_paint(a_turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draw a small rectangle whose bottom left corner is at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    a_turtle.begin_fill()
    a_turtle.speed(0)
    a_turtle.pencolor("white")
    a_turtle.fillcolor(51, 206, 205)
    a_turtle.forward(width)
    a_turtle.left(90)
    a_turtle.forward(length)
    a_turtle.left(90)
    a_turtle.forward(width)
    a_turtle.left(90)
    a_turtle.forward(length)
    a_turtle.left(90)
    a_turtle.end_fill()


def draw_paint_two(a_turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draw a small rectangle whose bottom left corner is at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    a_turtle.begin_fill()
    a_turtle.speed(0)
    a_turtle.pencolor("white")
    a_turtle.fillcolor(51, 206, 205)
    a_turtle.forward(width)
    a_turtle.right(90)
    a_turtle.forward(length)
    a_turtle.right(90)
    a_turtle.forward(width)
    a_turtle.right(90)
    a_turtle.forward(length)
    a_turtle.right(90)
    a_turtle.end_fill()


def draw_three_point_line(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a semi-circle that begins at point x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(90)
    a_turtle.pendown()

    a_turtle.pencolor("black")
    a_turtle.speed(0)
    i: int = 0
    while i < 180:
        a_turtle.forward(3)
        a_turtle.left(1)
        i = i + 1


def draw_three_point_line_two(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a semi-circle that begins at point x, y."""
    a_turtle.speed(0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(270)
    a_turtle.pendown()

    a_turtle.pencolor("black")
    a_turtle.speed(0)
    i: int = 0
    while i < 180:
        a_turtle.forward(3)
        a_turtle.left(1)
        i = i + 1
    

def draw_center_circle(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a full circle that begins at point x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    a_turtle.begin_fill()
    a_turtle.speed(0)
    a_turtle.pencolor("black")
    a_turtle.fillcolor(51, 206, 205)
    i: int = 0
    while i < 360:
        a_turtle.forward(0.9)
        a_turtle.right(1)
        i = i + 1
    a_turtle.end_fill()


def draw_basketball(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a small ball inside the center circle beginning at point x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    a_turtle.begin_fill()
    a_turtle.speed(0)
    a_turtle.pencolor("black")
    a_turtle.fillcolor("orange")
    i: int = 0
    while i < 360:
        a_turtle.forward(0.2)
        a_turtle.right(1)
        i = i + 1
    a_turtle.end_fill()
    if x < 0:
        a_turtle.penup()
        a_turtle.goto(-30, 13)
        a_turtle.setheading(0.0)
        a_turtle.pendown()
        a_turtle.goto(-30, -7)

        a_turtle.penup()
        a_turtle.goto(-25, 15)
        a_turtle.setheading(0.0)
        a_turtle.pendown()
        a_turtle.goto(-25, -8)

        a_turtle.penup()
        a_turtle.goto(-20, 13)
        a_turtle.setheading(0.0)
        a_turtle.pendown()
        a_turtle.goto(-20, -7)

        a_turtle.penup()
        a_turtle.goto(-35, 3)
        a_turtle.setheading(0.0)
        a_turtle.pendown()
        a_turtle.goto(-14, 3)
    else:
        a_turtle.penup()
        a_turtle.goto(30, 13)
        a_turtle.setheading(0.0)
        a_turtle.pendown()
        a_turtle.goto(30, -7)

        a_turtle.penup()
        a_turtle.goto(25, 15)
        a_turtle.setheading(0.0)
        a_turtle.pendown()
        a_turtle.goto(25, -8)

        a_turtle.penup()
        a_turtle.goto(20, 13)
        a_turtle.setheading(0.0)
        a_turtle.pendown()
        a_turtle.goto(20, -7)

        a_turtle.penup()
        a_turtle.goto(35, 3)
        a_turtle.setheading(0.0)
        a_turtle.pendown()
        a_turtle.goto(14, 3)


if __name__ == "__main__":
    main()




        










        
