class StringUtility:
  def __init__(self,string):
   self.string = string

  def __str__(self):
    return self.string

  def vowels(self):
     num_vowels=0
     for char in self.string:
       if char in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
          num_vowels = num_vowels+1
       
         
       if num_vowels > int(5):
            print ("many")
            
   
    
         
   