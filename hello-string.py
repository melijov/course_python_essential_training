#!/usr/bin/env python3

def main():
  string_test()

  
  
def string_test():
  #string methods
  print('Hello, World.'.upper())
  print('Hello, World.'.lower())
  print('Hello, World.'.capitalize())
  print('Hello, World.'.title())
  print('Hello, World.'.swapcase())
  print('Hello, World.'.casefold())
  #String is inmutable
  s1 = 'Hello, World.'
  s2 = s1.lower()
  
  #litteral concatenation
  print(s1 is s2)
  s3  = 'this string' ' that string' #concatenation of litteral strings
  print(s3)
  

  
  # format method
  x = 42
  y=53
  print('the numbers are {} {}'.format(x,y))  #in order
  print('the numbers are {bb} {xx}'.format(xx=x,bb=y))
  print('the numbers are {0} {1} {0}'.format(x,y))  #positional arguments
  
  #leading zeros
  print('the numbers are {0:<5} {1:+05}'.format(x,y))  # formatting instructions preceded by a :
  
  #comma style
  x = 42 * 747 * 1000
  print('the numbers are {:,}'.format(x))
  
  # comma style converted to . style
  print('the numbers are {:,}'.format(x).replace(',','.'))
  # fixed number of decimal places
  print('the numbers are {:f}'.format(x))
  # 3 number of decimal places
  print('the numbers are {:.3f}'.format(x))
  
  x = 42
  # different basis x is hexadecimal, o octal, b binary
  print('the numbers is {:x} hexadecimal'.format(x))
  print('the numbers is {:o} octal'.format(x))
  print('the numbers is {:b} binary'.format(x))
  
  #beginning python 3.6 we now use f string for formatting
  print(f'the number is {x}')
  print(f'the number is {x:3f}')
  
  
  print('Hello, World. {}'.format(42*7))
  print("""
        Hello, 
        World. 
        {}
        """.format(42*7))
  s = 'Hello, World. {}'
  print(s.format(42 * 7))
  
  # string inheritance
  class MyString(str):
    def __str__(self):
      return self[::-1]
  
  s = MyString('Hello, World.')
  print(s)


  
  
  
if __name__ == '__main__':main()