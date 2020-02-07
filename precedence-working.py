#!\usr\bin\env python3

def main():
  print('precedence-working.py main()')
  
  precedence =('**',('+x','-x'),('*','/','//','%'),('+','-'),('<<','>>'),'&','^','|',('in','not in','is','is not','<','<=','>','>=','!=','=='),'not x', 'and', 'or')
  print('\t Operator Precedence')
  for p in precedence:
    print(p)
  
  
  
  
if __name__ == '__main__': main()