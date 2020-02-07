#!/usr/bin/env python3
import platform
import sys

def main():
  try:
    #x = int('foo')
    #x=5/0
    #x=5/3
    foo()
  except ValueError:
    print('I cought a ValueError')
  except ZeroDivisionError:
    print('don\'t divide by zero')
  except:
    print(f'unknown error: {sys.exc_info()[1]}')
  else:
    print('Good job')
    print(x)
  print('This is python version {}'.format(platform.python_version()))
  
if __name__=='__main__':
  main()