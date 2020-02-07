#!/usr/bin/env python3

def main():
  print(f'{__file__}')
  s = 'This is a long string with a bunch of words in it.'
  print(s)
  s = '''This is a long string
  with a bunch of words 
  in it.'''
  
  print(s.split())
  print(s.split('i'))
  
  l = s.split()
  s2 = ':'.join(l)
  print(s2)
  
  s2 = '  -- '.join(l)
  print(s2)
  
  a= 1
  b =-1
  print('{1:<+04} {0:+04}'.format(a,b))
  
  s1='Test'
  s2='tEST'
  
  s1.capitalize()==s2.capitalize()
  
if __name__ == '__main__':main()