#!/usr/bin/env python 3

def main():
  print ('types-working.py main()')

  x = 7
  x = (1,2,3,4,5)
  x = (1,'two',3.0,[4,'four'],5)
  y = (1,'two',3.0,[4,'four'],5)
  
  print('x is {}'.format(x))
  print(type(x))
  print(type(x[1])) # this is string
  

  #-------------------------
  
  x = '47'
  y = int(x) # int constructur
  z = float(x) # float constractor
  a= -47
  b=abs(a)
  c=divmod(47,3)  # tuple (dividend, mode)
  d=complex(47,3) # complex constructor numbers
  e= 47 +73j  # complex numbers
  
  print(f'x is {type(x)}')
  print(f'x is {x}')
  print(f'y is {type(y)}')
  print(f'y is {y}')
  print(f'z is {type(z)}')
  print(f'z is {z}')
  print(f'c is {type(c)}')
  print(f'c is {c}')
  print(f'd is {type(d)}')
  print(f'd is {d}')
  print(f'e is {type(e)}')
  print(f'e is {e}')  
  
  
if __name__ == '__main__': main()