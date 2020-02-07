#!/usr/bin/env python3

def main():
  print('bitwise-working.py main()')
  print('& And, | Or, ^ Xor, << Shift Left, >> Shift Right')
  x = 0x0a
  y = 0x01
  z = []
  z.append( x & y) # and
  z.append(x | y)
  z.append(x ^ y) # one or the other ar true not both
  z.append(x << y) # shift left
  z.append(x >> y) # shift right
  
  for i in z:
    print(f'(hex) x is {x:02x}, y is {y:02x}, z i {i:02x}')
    print(f'(bin) x is {x:08b}, y is {y:08b}, z i {i:08b}')

  
if __name__=='__main__': main()