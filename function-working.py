#!\usr\bin\env python 3
# Python does not support forward declarations

def main():
#in Python a call is always made by reference
#so if a Mutable object (list) is passed as an argument and it is changed in the called function it will change as well in the calling function
#if an unmutable object is passed as an argument and it is changed a new object will be created in the called function and the object in the calling function will not change

  x = [5]  
  y=kitten(x) 
  print(f' in main x is {x}')
  print(type(y),y)
 
#Arguments with default must be at the end of the argument list 
def kitten(a=0,b=0,c=0):

  a[0] = 3
  print('Meow.')
  print(a)
  #return 42
  #return [42]
  
  return dict(x=42,y=43)
  
if __name__=='__main__': main()  #__name__ returns the name of the current module! if it is not in a module then returns __main__