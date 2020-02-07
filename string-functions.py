def main():

  string_functions()
  
class kitten:
  def __init__(self, n):
    self._n = n
  
class bunny:
  def __init__(self, n):
    self._n = n
  def __repr__(self):
    return f'repr: the number of bunnies is {self._n}'
    
  def __str__(self):
    return f'str: the number of bunnies is {self._n}'
 

 
def string_functions():
  s = 'Hello, World.'
  print(repr(s))  # __repr__ representation of the object
  print(s)        # __str__ representation of the object
  k= kitten(47)
  b = bunny(47)
  
  print(repr(k))  # if no specific __repr__ method is defined the default value is returned
  print(repr(b))  # __repr__ representation of the object 
  print(b)        # __str__ representation of the object (if __str__ is not defined it will pick __repr__ value)
  
  print(ascii(b))  # ascii works like __repr__ but converts any special characters into an escaped sequence
  print(chr(128406))  # prints the character of a number
  print(ord(chr(128406))) # prints the number of a character
  
  
if __name__ == '__main__':main()