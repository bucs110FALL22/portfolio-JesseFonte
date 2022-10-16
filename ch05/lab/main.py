import pygame 

def num_sequence(n):
  sequence = [n]
  count = (0)
  
  if n < 1:
   return []
  
  while n > 1: 
    if n % 2 == 0:
      n = n /2 
      
    else: 
      n = 3 * n + 1
    
    
    count += 1
  
    sequence.append(n)
  return (count, sequence) 
  

print(num_sequence(101))




upperLimit= 20
iters = {}


start = range(2,upperLimit+1)

for i in start:

  print (num_sequence(i))
  count, _ =  (num_sequence(i))
  
  iters[i] = count 
  

print (iters)
  


pygame.init()

display = pygame.display.set_mode()

upperLimit = 20
iters = {}
maxSofar = 0 
maxVal = 19
scale = 5
n = 101

for i in range(2,upperLimit +1):
  count  = 0 
while n > 1:
  if n % 2 ==0:
    n = n/2
  else:
    n = n * 3 + 1
  count += 1
  iters[n] = count 
  iters.items()
  print(iters)
pygame.draw.line(display,"pink",True,2)  



  

  
