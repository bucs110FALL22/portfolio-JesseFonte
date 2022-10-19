def mult(a = 0, b = 0):
  result = 0  
  for i in range(a):
    result += b
  return result 

def exp(e = 0, t = 0):
  result = 1
  for i in range(t):
    result *= e
  return result 

def square(c=0):
  return exp(c, 2)

def main():
  print(mult(5,9))
  print (exp(10,6))
  print (square(9))

main()