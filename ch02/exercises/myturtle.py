import turtle 
my_turtle = turtle.Turtle()
Window = turtle.Screen()
my_turtle.shape("turtle")
my_turtle.color("purple")
length = 50
turn = 90
for i in range (4):
  my_turtle.fd(length)
  my_turtle.left(turn)
my_turtle.up()
my_turtle.right(180)
my_turtle.fd (length)
my_turtle.color("red")
my_turtle.down()
for i in range (4):
  my_turtle.fd(length)
  my_turtle.left(turn) 













Window.exitonclick()