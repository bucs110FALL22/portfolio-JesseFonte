import turtle #1. import modules
import random

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
ill = random.randrange(1,101)
pill = random.randrange (1,101)
michelangelo.forward(ill)
leonardo.forward(pill)


michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

chel = random.randrange (0,10)
nel = random.randrange (0,10)
                     
                      
for i in range(10): 
  michelangelo.forward(chel)
  leonardo.forward(nel)
 
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


window.exitonclick()

# PART B - complete part B here

pygame.init()
window = pygame.display.set_mode()
pygame.draw.polygon

coords = []

num_sides = (3)

side_length = 100

offset = 100

for i in range(num_sides):
  theta = 2.0 * math.pi * (i) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  points = [x,y]
  coords.append(points)
    
pygame.draw.polygon(window,"red",coords)
pygame.display.flip()
window.fill("black")
pygame.time.wait(2000)


num_sides = (4)
coords=[]
for i in range(num_sides):
    theta = 2.0 * math.pi * (i) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    points = [x,y]
    coords.append(points)
      
pygame.draw.polygon(window,"blue",coords)
pygame.display.flip()
window.fill("black")
pygame.time.wait(2000)

num_sides = 6
coords= []
for i in range(num_sides):
    theta = 2.0 * math.pi * (i) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    points = [x,y]
    coords.append(points)
      
pygame.draw.polygon(window,"yellow",coords)
pygame.display.flip()
window.fill("black")
pygame.time.wait(2000)


num_sides = 9 
coords = []
for i in range(num_sides):
    theta = 2.0 * math.pi * (i) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    points = [x,y]
    coords.append(points)



  
pygame.draw.polygon(window,"pink",coords)
pygame.display.flip()
window.fill("black")
pygame.time.wait(2000)



num_sides = 360
coords = []
for i in range(num_sides):
    theta = 2.0 * math.pi * (i) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    points = [x,y]
    coords.append(points)



  
pygame.draw.polygon(window,"pink",coords)
pygame.display.flip()
window.fill("black")
pygame.time.wait(2000)