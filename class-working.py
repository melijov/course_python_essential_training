#!/usr/bin/env python3

"""

A class is the basis for all data in Python
Everything is an object in Python
A class is how an object is defined

"""

class Duck:
  sound = 'Quack quack.'
  movement = 'Walks like a duck.'
  
  #objects methods
  def quack(self):   #self is a reference to the object (instance) not the class
    print(self.sound)
    
  def move(self):    #self is a reference to the object (instance) not the class
    print(self.movement)
    
def main():
  donald = Duck()
  donald.quack()
  donald.move()



if __name__=='__main__':main()