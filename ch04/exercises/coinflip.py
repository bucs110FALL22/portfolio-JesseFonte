import random 
import turtle 

myturtle = turtle.Turtle()
myturtle.shape('turtle')
myturtle.color('purple') 
window = turtle.Screen()
window.setup(300,300) 
window.bgcolor('pink')

true = True 

while true is True:
  flip = random.randrange(1,3)
  print (myturtle.xcor(), myturtle.ycor())
  if flip == 1:
    myturtle.right(90)
  elif flip == 2:
    myturtle.left(90) 
  myturtle.fd(50) 
  print (myturtle.xcor(), myturtle.ycor())
  if myturtle.xcor() >= 150 or myturtle.xcor() <= -150:
     true = False 
  elif myturtle.ycor() >= 150 or myturtle.ycor() <= -150:
     true = False 
  
  


window.exitonclick()
