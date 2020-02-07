#!/usr/bin/env python3

def main():
  print('boolean-working.py main()')
  print('and, or, not, in (value in set), not in (value not in set), is (same object identity), is not (not same object identity)')
  a = True
  b = False
  x = ('bear','bunny', 'tree', 'sky', 'rain')
  y = 'bear'
  
  if a and  b:
    print(f'{a} and {b} is true')
  else:
    print(f'{a} and {b} is false')
    
  if a or  b:
    print(f'{a} or {b} is true')
  else:
    print(f'{a} or {b} is false')
  
  if not a:
    print(f'not {a} is true')
  else:
    print(f'not {a} is false')
    
  if y in x:
    print(f'{y} in {x} is true')
  else:
    print(f'{y} in {x} is false')
    
  if y not in x:
    print(f'{y} not in {x} is true')
  else:
    print(f'{y} not in {x} is false')
    
  if y is  x[0]:
    print(f'{y} is {x[0]} is true')
  else:
    print(f'{y} is {x[0]} is false')
    
  if 'bear' is not  x[0]:
    print(f'bear is not {x[0]} is true')
  else:
    print(f'bear is not {x[0]} is false')
  
if __name__ == '__main__': main()