#!usr/bin/env python3
# the file object is an iterator
# rstrip strips all the whiteline characters from the end of the string
# open by default is r: read mode, w: if the file does not exist it creates the file, a: append mode. Optional + read and write, Optional t or b: text or binary mode

def main():
  print(f'{__file__}')
  f = open('lines.txt','r')
  for line in f:
    print(line.rstrip()) #stripping the new line at the end of the line
    
  f.close()
  
if __name__ == '__main__':main()