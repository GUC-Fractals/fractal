import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Dragon")

turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)

r = "R"
l = "L"
temp = [r]
iteration = 1

while iteration < 13:
    # add a right to the end of the old iteration
    moves = temp + [r]

    # if the middle character is r:
    if temp[int((len(temp) - 1) / 2)] == r:
        # change it to a l
        temp[int((len(temp) - 1) / 2)] = l

    # otherwise, if it is l:
    elif temp[int((len(temp) - 1) / 2)] == l:
        # change it to r
        temp[int((len(temp) - 1) / 2)] = r

    moves = moves + temp
    temp = moves
    iteration += 1

colors = ["medium purple", "blue violet", "dark violet", "dark orchid", "medium orchid", "orchid", "plum", "thistle",
          "light gray", "gainsboro"]
color = 0
portion = int(len(moves) / len(colors))  # dividing colors evenly among all moves
pcounter = 0

for c in moves:

    turtle.color(colors[color])

    if c == "L":
        turtle.left(90)
    elif c == "R":
        turtle.right(90)
    turtle.forward(3)

    # for coloring
    pcounter += 1

    if pcounter == portion:
        pcounter = 0
        color += 1  # change color
        if color == len(colors):
            color -= 1

turtle.up()
turtle.done()
