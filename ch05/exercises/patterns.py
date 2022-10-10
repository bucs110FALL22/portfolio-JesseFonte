def star_pyramid(): 
  rows = int(input("How many rows?"))
  
  for i in range(rows):
    print("*" * (i+1))
  
  

star_pyramid()


def rstar_pyramid():
  row = int(input("How many rows?")) 

  for i in reversed(range(row)):
    print ("*" * (i+1))

rstar_pyramid()
