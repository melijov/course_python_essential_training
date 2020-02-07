#!/usr/bin/env python3


def main():
  x =42
  print('Hello, world. %d' % x) # deprecated use format and {} instead
  print('Hello, World. {}'.format(x))
  print(f'Hello, World. {x}') # this is the new way to use since version 3.6
  

  
if __name__=='__main__':
  main()