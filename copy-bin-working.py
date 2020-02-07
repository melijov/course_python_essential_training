#!/usr/bin/env python3

def main():
  infile = open('pack_of_wolves.jpg','rb')
  outfile = open ('pack_of_wolves_copy.jpg','wb')
  while True:
    buf = infile.read(10240)  # read the file 10K at a time, just in case if there is not enough memory available
    if buf:
      outfile.write(buf)
      print('.',end='',flush=True)
    else: break  # if the buffer is empty we break out of the loop
  outfile.close()
  print('\ndone.')
  
if __name__=='__main__':main()