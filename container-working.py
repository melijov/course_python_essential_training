#!/usr/bin/env python3

def main():
  container_test()
  
  
def container_test():
  x = (1,2,3,4,5)
  z= (6,7,8,9,10)
  a = ('cat', 'dog', 'rabbit', 'velociraptor')
  y = x
  print(x)
  print(y)  
  y = len(x)
  print(y)
  
  y = reversed(x)   #returns an iterator
  print(y)
  
  y = tuple(reversed(x)) # reversed tuple
  print(y)
  y = list(reversed(x)) # reversed list
  print(y)
  y = sum(x)
  print(y)
  y = sum(x, 10)  # 10 is the starting value of the sum + all the values in x
  print(y)
  y = max(x)
  print(y)
  y= min(x)
  print(y)
  y = any(x)  # any: returns True if any element is True
  print(y)
  y = all(x)  #all: returns True if all elements are True
  print(y)
  y= zip(x,z)  # returns an iterator
  print(y)
  y = tuple(zip(x,z)) # returns a tuple of tuples
  print(y)
  y = list(zip(x,z)) # returns a list of tuples
  print(y)
  y = dict(zip(x,z)) # returns a dictionary: where the elements of the first tuple are keys and the elements of the second tuple are the values
  print(y)
  
  y = enumerate(x) # returns an iterator
  print(y)
  y = tuple(enumerate(a)) # a tuple of tuples where the first element is the index and the second the value
  print(y)
  y = list(enumerate(a)) # a list of tuples where the first element is the index and the second the value
  print(y)
  y = dict(enumerate(a)) # a dictionary where the first element is the index and the second the value
  print(y)
  
  
if __name__ == '__main__':main()