from turtle import *

def draw(size, angle, levels):
    if levels == 0:
        return
    forward(size)
    right(angle)
    draw(size*.99, angle*.99, levels-1)

draw(100, 60, 100)
mainloop()
