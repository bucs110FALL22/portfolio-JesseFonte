import turtle 

draw = turtle.Turtle()
window = turtle.Screen()
draw.speed(150)


def hypnosis():
  distance = 0  
  for i in range(100):
    draw.forward(distance)
    draw.left(90)
    draw.pencolor("red")
    distance += 6
  return distance

def main():
  print(hypnosis())
  draw.up()
  draw.home()
  draw.down()
  distance = 0
  for i in range(100):
    draw.forward(distance)
    draw.right(90)
    draw.pencolor("red")
    distance += 6

print (main())























window.exitonclick()
