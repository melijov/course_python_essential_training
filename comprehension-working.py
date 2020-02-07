#!/usr/bin/env python3

def main():
  from math import pi
  """ 
  A list comprenhension is a list created based on another list or another iterator
  """
  seq = range(11)
  seq2=[x * 2 for x in seq]   #list comprehension
  seq3=[x for x in seq if x % 3 != 0] # list comprehension with if after for
  seq4=[(x,x**2) for x in seq] # list comprehension with tuples
  seq5=[round(pi,x) for x in seq] # list comprehension with a function call
  seq6 = {x: x**2 for x in seq} #list comprehension within a dictionary
  seq7 = {x for x in 'superduper' if x not in 'pd'} # set: unique members
  print_list(seq)
  print_list(seq2)
  print_list(seq3)
  print_list(seq4)
  print_list(seq5)
  print(seq6)
  print(seq7)
  print_list(seq7)
  
def print_list(o):
  for x in o:print(x,end=' ')
  print()
  
if __name__=='__main__':main()