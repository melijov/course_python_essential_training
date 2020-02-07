def main():
  """
  Set is like a list that does not allow duplicate elements
  """
  a = set("We're gonna need a bigger boat.")
  b = set("I'm sorry, Dave. I'm afraid I can't do that.")
  print_set(sorted(a))
  print_set(sorted(b))
  print_set(a - b) # members in a but not in b
  print_set(b - a) # members in b but not in a
  print_set(a | b) # members in a, b or in both
  print_set(a ^ b) # members in a, b but not in both
  print_set(a & b) # members in a and b
  
 
def print_set(o):
  print('{',end=' ')
  for x in o: print(x,end=' ')
  print('}')

if __name__=='__main__':main()