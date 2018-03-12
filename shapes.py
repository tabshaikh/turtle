import turtle


def square():
    screen = turtle.Screen()
    screen.bgcolor("white")

    tab = turtle.Turtle()
    tab.shape("turtle")
    tab.speed(0.5)
    tab.color("green")

    for i in range(1, 37):
        for i in range(1, 5):
            tab.forward(100)
            tab.right(90)
        tab.right(10)

    screen.exitonclick()


square()
