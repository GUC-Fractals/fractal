import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(1)
turtle.colormode(255)

iter = 1

while iter<350:
    #colors
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.color((r,g,b))


    turtle.forward(iter + 20)
    turtle.left(70.991)

    iter+=1

turtle.up()
turtle.done()
