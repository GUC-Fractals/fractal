import turtle
import time
turtle.speed('fastest')
turtle.color('purple')

def levy(l, n):
    if n == 0:
        turtle.forward(l)
        return
    turtle.left(45)
    levy(l*2**0.5/2, n-1)
    turtle.right(90)
    levy(l*2**0.5/2, n-1)
    turtle.left(45)

def change_pos(lenght):
    turtle.penup()
    turtle.left(180)
    turtle.forward(lenght/2)
    turtle.left(90)
    turtle.forward(lenght/4)
    turtle.left(90)
    turtle.pendown()

lenght = 400

change_pos(lenght)

levy(lenght, 12)

time.sleep(9999) 