import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()


def TurtleDrawing():
    turtle_instance.forward(50)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading()-10)
    #turtle_instance.left(20)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading() + 10)
    #turtle_instance.left(20)

def clear_seecren():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

def turtle_pen_down():
    turtle_instance.pendown()

def turtle_pen_up():
    turtle_instance.penup()


drawing_board.listen()
drawing_board.onkey(fun=TurtleDrawing, key="space")
drawing_board.onkey(fun=rotate_angle_left, key="a")
drawing_board.onkey(fun=rotate_angle_right, key="d")
drawing_board.onkey(fun=clear_seecren, key="c")
drawing_board.onkey(fun=turtle_return_home, key="h")

drawing_board.onkey(fun=turtle_pen_up, key="w")
drawing_board.onkey(fun=turtle_pen_down, key="s")

turtle.mainloop()