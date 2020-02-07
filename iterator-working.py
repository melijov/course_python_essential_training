#!/usr/bin/env python3

#An iterator is a class that provides a sequence of items usually employed in a loop
#Yield was implemented after iterators. Yield function is used in generators.
#Iterators are the same as generators. Generators are easies to implemtn

class inclusive_range:
  def __init__(self,*args):
    numargs = len(args)
    self._start = 0
    self._step = 1
    
    if numargs < 1:
      raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
      self._stop = args[0]
    elif numargs == 2:
      (self._start, self._stop) = args
    elif numargs == 3:
      (self._start, self._stop, self._step) = args
    else: raise TypeError(f'expected at most 3 argumentes, got {numargs}')
    self._next = self._start
  
  def __iter__(self):
    return self
    
  def __next__(self):
    if self._next > self._stop:
      raise StopIteration
    else:
      _r = self._next
      self._next += self._step
      return _r

  def __str__(self):
    s = f'['
    for n in self:
      s += f'{n}, '
    s = s[:-2] + ']'
    return s
   
def test_iterator():
  print(inclusive_range(30))
  print(inclusive_range(5,30))
  print(inclusive_range(5,30,5))
  #print(inclusive_range())
  print(inclusive_range(25,50,34,56))
  

def main():
  print(f'{__file__}')
  test_iterator()
 
  
  
  
if __name__ == '__main__': main()