from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def move_clockwise():
    turtle.setheading(turtle.heading()+ 15)


def move_counterclockwise():
    turtle.setheading(turtle.heading()-15)


def clear():
    turtle.clear()


screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_clockwise, "d")
screen.onkey(move_counterclockwise, "a")
screen.onkey(clear, "c")
screen.listen()
screen.exitonclick()
