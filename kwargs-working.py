#!\usr\bin\env python 3

#Keyword Arguments: diction instead of a tuple

def main():
  kitten(Buffy='meow',Zilla='grr',Angel='rawr')
  x = dict(Buffy='meow',Zilla='grr',Angel='rawr')
  kitten(**x)
  
def kitten(**kwargs):
  if len(kwargs):
    for k in kwargs:
      print('Kitten {} says {}'.format(k,kwargs[k]))
  else:
    print('Meow.')
    
if __name__=='__main__':main()