import turtle

minBranchLength = 5

def buildTree(tree, branchLength, shortenBy, angle):
    if(branchLength > minBranchLength):
        tree.forward(branchLength)
        newLength = branchLength - shortenBy

        tree.left(angle)
        buildTree(tree, newLength, shortenBy, angle)

        tree.right(angle*2)
        buildTree(tree, newLength, shortenBy, angle)

        tree.left(angle)
        tree.backward(branchLength)

tree = turtle.Turtle()
tree.hideturtle()
tree.setheading(80)
tree.color('blue')

buildTree(tree, 50, 5, 30)
turtle.mainloop()