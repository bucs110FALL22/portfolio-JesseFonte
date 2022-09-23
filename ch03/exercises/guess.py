import random 

random = random.randrange(1,11)


for i in range(3): 
  guess = int(input("What is your guess?"))
  if (guess == random):
    print ("correct!")
    break
  
  elif (guess < random):
    print ("Too Low")

  elif (guess > random):
    print ("Too High") 

 
