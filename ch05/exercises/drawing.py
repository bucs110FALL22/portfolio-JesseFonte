import turtle 

def drawEqShape(t, l, s):

  for i in range(s):
    t.forward(l)
    t.left(360/s) 

num_sides = int(input("How many sides?"))
side_length = int(input("Length of sides?"))



turt = turtle.Turtle()
window = turtle.Screen()
turt.shape("turtle")
turt.color("green")

drawEqShape (turt, side_length, num_sides)


window.exitonclick()