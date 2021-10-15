import turtle

def kochCurve(curve, iterations, length, shorteningFactor, angle):
    if iterations == 0:
        curve.forward(length)
    else:
        iterations = iterations - 1
        length = length / shorteningFactor

        kochCurve(curve, iterations, length, shorteningFactor, angle)
        curve.left(angle)
        kochCurve(curve, iterations, length, shorteningFactor, angle)
        curve.right(angle * 2)
        kochCurve(curve, iterations, length, shorteningFactor, angle)
        curve.left(angle)
        kochCurve(curve, iterations, length, shorteningFactor, angle)


curve = turtle.Turtle()
curve.hideturtle()

for i in range(3):
    kochCurve(curve, 4, 200, 3, 60)
    curve.right(120)
turtle.mainloop()
