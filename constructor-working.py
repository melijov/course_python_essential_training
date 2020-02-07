#!/usr/bin/env python3

class Animal:
  #the self makes it an object method
  """
  #positionned parameters
  def __init__(self, type, name, sound):
    #object variables: they do not exist in the class without being it constructed into an object
    #the _ at the beginning of the name is a traditional naming convention. It discourages to access directly these object variables
    self._type = type  
    self._name = name
    self._sound = sound
  """  
  #named parameters
  def __init__(self, **kwargs):
    #object variables: they do not exist in the class without being it constructed into an object
    #the _ at the beginning of the name is a traditional naming convention. It discourages to access directly these object variables
    self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
    self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
    self._sound = kwargs['sound'] if 'sound' in kwargs else 'rawr'
  
  
  #Accessors or Gettors which simple return the value of the object variables
  def type(self):
    return self._type
    
  def name(self):
    return self._name
    
  def sound(self):
    return self._sound
    
def print_animal(o):
  if not isinstance(o,Animal):
    raise TypeError('print_animal(): requires and Animal')
  print(f'The {o.type()} is named {o.name()} and says {o.sound()}')
  
def main():

  #a0 = Animal('kitten', 'fluffy','rwar')
  #a1 = Animal('duck', ' donald', 'quack')
  a0 = Animal(type='kitten', name='fluffy',sound='rwar')
  a1 = Animal(type='duck', name=' donald', sound='quack')
  print_animal(a0)
  print_animal(a1)

  print_animal(Animal(type='velociraptor', name='veronica', sound='hello'))
  print_animal(Animal())
  
if __name__ == '__main__':main()