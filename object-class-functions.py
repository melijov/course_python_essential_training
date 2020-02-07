def main():
  test_object_class_functions()
  
def test_object_class_functions():
  x = 42
  y = type(x) #returns the class and type of the object
  
  print(x)
  print(y)
  y = isinstance(x, int)
  print(y)
  y=id(x)
  print(y)
  
if __name__ == '__main__':main()