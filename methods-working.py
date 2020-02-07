#!/usr/bin/env python 3

# A function that is associated with a class is called a method
# Methods are identical to functions except for the fact that they are bound to an object through the first parameter usually named self
class Animal:
  def __init__(self, **kwargs):
    #object variables: they do not exist in the class without being it constructed into an object
    #the _ at the beginning of the name is a traditional naming convention. It discourages to access directly these object variables
    self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
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
  #a0 = Animal('kitten', 'fluffy','rwar')
  #a1 = Animal('duck', ' donald', 'quack')
  a0 = Animal(type='kitten', name='fluffy',sound='rwar')
  a1 = Animal(type='duck', name=' donald', sound='quack')
  a0.sound('bark')
  print(a0)
  print(a1)

  print(Animal(type='velociraptor', name='veronica', sound='hello'))
  #print_animal(Animal())
  
  
if __name__ == '__main__':main()