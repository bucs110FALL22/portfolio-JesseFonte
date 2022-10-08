import pygame 
import math 
import random 
from tkinter import EventType 

pygame.init()

window = pygame.display.set_mode((500,250))

x = 500

y = 250

pygame.draw.rect(window, "green", (0,0,250,500), 0)
pygame.draw.rect(window, "red", (250,0,250,500), 0)
pygame.display.flip()
playerChoice = "" 

print("Who do you think will win?")

print("Green or Red Please click.")

getGuess = True 

while getGuess: 
  for event in pygame.event.get(): 
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.pos[0] < 250:
        playerChoice = "green"
        getGuess = False
      elif event.pos[0] > 250:
        playerChoice = "red"
        getGuess = False 
  print (playerChoice) 
  pygame.time.wait(5000)


pygame.draw.circle(window,"red", (260,100), 200 , 0)
pygame.draw.line(window,("black"), (250,0), (250,250), 5)
pygame.draw.line(window, ("black"), (50, 110), (1000, 110), 5)

for i in range(10):
  green_score = 0
  red_score = 0 
  print("Green throws")
  dartwhereX = random.randrange(0,500)
  dartwhereY = random.randrange(0,500)
  distance_from_center = math.hypot(dartwhereX-250, dartwhereY-250)
  is_in_circle = distance_from_center <= 500/2
  if is_in_circle == True:
    pygame.draw.circle(window, "blue", (dartwhereX, dartwhereY), 5)
    print("hit")
    green_score +=1
  else:
    pygame.draw.circle(window, "black", (dartwhereX, dartwhereY), 5)
    print("Miss")
    green_score -=1
  dartwhereX = random.randrange(0,500)
  dartwhereY = random.randrange(0,500)
  print ("Green throws")
  distance_from_center = math.hypot(dartwhereX-250, dartwhereY-250)
  is_in_circle = distance_from_center <= 500/2
  if is_in_circle == True: 
    pygame.draw.circle(window, "blue", (dartwhereX, dartwhereY), 5)
    print("hit")
    red_score +=1
  else:
    pygame.draw.circle(window, "black", (dartwhereX, dartwhereY), 5)
    print("Miss")
    red_score -=1
if playerChoice == "Green" and green_score > red_score:
  print ("Correct")
elif red_score < green_score:
  print ("Wrong")
else: 
  print ("It's a tie")

pygame.display.update()
pygame.time.wait(5000)
    
  

                            
pygame.display.flip()
