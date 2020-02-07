#!\usr\bin\env python3

def main():
  print('while-working.py main()')
  secret = 'swordfish'
  pw = ''
  
  while pw !=secret:
    pw = input('What is the secret word?')
  
  print(f'The secret word is {secret}')

  
if __name__ == '__main__': main()