#!\usr\bin\env python3

def main():
  print('for-working.py main()')
  languages = ('Bulgarian','Russian', 'Spanish', 'French','English','Portuguese','Italian')
  
  for language in languages:
    print(language)
    
  for i in range(7):
    print(i)
  
if __name__ == '__main__': main()