#!/usr/bin/env python3
#to write to a file you can use print or writelines
#print + .rstrip will allow to remove the original line endings and replace them with the line ending of the new operational system. writelines does not do that
def main():
  infile = open('lines.txt','rt')  #read mode and text mode : default 
  outfile = open('lines-copy.txt','wt') # write mode and text mode
  for line in infile:
    #print(line.rstrip(),file=outfile)  #rstrip to strip the endings, it is printing to the output file
    outfile.writelines(line)
    print('.',end=' ', flush=True)  #flush output buffer
  outfile.close()
  infile.close()
  print('\ndone.')
  
if __name__ == '__main__':main()