import turtle 
draw = turtle.Turtle()
window = turtle.Screen()


sides = int(input("How many sides would you like?"))
length = int(input("How long each side?"))

draw.shape("turtle")clear
draw.color("red")

for i in range(sides):
  draw.forward(length)
  draw.left(360/sides) 





















window.exitonclick()