#!/usr/bin/env python3


class Animal:
  x = [1,2,3] # class variable define in the class. Encapsulation. If the variable is encapsulated then it belongs to the object and not to the class
  #it is a bad idea to add mutable variables to the class
  
  def __init__(self, **kwargs):
    self._type = kwargs['type'] if 'type' in kwargs else 'kitten' #object variable
    self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
    self._sound = kwargs['sound'] if 'sound' in kwargs else 'rawr'
   
  #Gettors/Settors Methods. The first parameter self makes this function into an object method
  #Python does not have private variables. The first underscore indicates that this variable should not be accessed outside of the class
  
  def type(self, t = None):
    if t: self._type = t # settor
    return self._type # gettor
    
  def name(self, n = None):
    if n: self._name = n
    return self._name
    
  def sound(self, s = None):
    if s: self._sound = s
    return self._sound
   
  #Special method: provides the string representation of the object
  def __str__(self):
    return f'Te {self.type()} is named "{self.name()}" and says "{self.sound()}".'

  
def main():

  a0 = Animal(type='kitten', name='fluffy',sound='rwar')
  a1 = Animal(type='duck', name=' donald', sound='quack')
  a0.sound('bark')
  
  print(a0)
  print(a1)
  print(a0.x)
  a0.x[0]=7 # the object a0 does not have x it is drowing it from the class
  print(a1.x)
  
  

  print(Animal(type='velociraptor', name='veronica', sound='hello'))
  #print_animal(Animal())
  
  
if __name__ == '__main__':main()



