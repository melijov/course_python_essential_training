#!/usr/bin/env python3
# sequences in python: list, tuple, range and dictionary
def main():
  print('sequence-working.py main()')
  x = [1,2,3,4,5] # a list, a mutable sequence
  x[2]=42 # a mutable sequence
  
  #It is better to favor tuples over lists
  x= (1,2,3,4,55) # a tuple is an unmutable sequence
  #x[2]=42 # error 'tuple' object does not support item assignment
  
  #Range is also a sequence inmutable
  #there are 3 parameters start, end, step
  
  x = range(5)
  x=range(5,50,10)
  
  #To make a range mutable we need to cast it to a list
  
  x = list(range(5))
  x[2]=42
  
  # a dictionary is a searchable and mutable sequence 
  x = {'one':1,'two':2, 'three':3, 'four': 4, 'five': 5}
  x['three'] = 42
  
  for k,v  in x.items(): # returns two tuples
    print('k: {}, v: {}'.format(k, v))
if __name__ == '__main__': main()