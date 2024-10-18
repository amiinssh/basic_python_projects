from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)
    
def move_lefts():
    tim.left(10)
    
def move_rights():
    tim.right(10)
    
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_lefts)
screen.onkey(key="d", fun=move_rights)
screen.exitonclick()