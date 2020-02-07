#!/usr/bin/env python3

def main():
  print('arithmetic-working.py main()')
  operators = {'+':'addition (unary positive)','-':'substraction (unary negative)','*':'multiplication','/':'division','//':'integer division','%':'remainder(modulo)','**':'exponent'}
  
  for k,v in operators.items():
    print (f'{k} \t-\t {v}')
    
  x = 5
  y = 3
  z =[]
  z.append(x + y)
  z.append( x - y)
  z.append(x * y)
  z.append(x / y)
  z.append(x // y)
  z.append(x % y)
  z.append(x ** y)
  z.append(x // y)
  z.append(+x)
  z.append(-x)
  
  for i in z:
    print(f'result is {i}')
  
if __name__ == '__main__': main()