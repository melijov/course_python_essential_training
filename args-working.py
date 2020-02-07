#!\usr\bin\env python 3
def main():
  x =('meow','grrr','purrr','hello')
  
  kitten(*x)  #this will pass a reference to x
  
  kitten('meow','grrr','purrr')
  kitten()
  
# *args is a variable lengh of arguments (a tuple)

def kitten(*args):
  if len(args):
    for s in args:
      print(s)
  else: print('Meow.')
  
if __name__=='__main__':main()