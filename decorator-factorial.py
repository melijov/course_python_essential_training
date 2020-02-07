def main():
  """
  Decorator case study with factorial
  The Decorator will be used to raise exception if the number is not positive and int
  
  """
  test_factorial()
  
  
def argument_test_natural_number(f):
  def helper(x):
    if type(x) == int and x > 0:
      return f(x)
    else:
      raise Exception(f'Argument {x} is not a positive integer')
  return helper

  
@argument_test_natural_number
def factorial(n):
  if n==1:
    return 1
  else:
    return n * factorial(n-1)
    
def test_factorial():
  for i in range(1,10):
    print(i,factorial(i))
    
  print(factorial(-1))
if __name__=='__main__': main()