import sys
import os
import random
import datetime

def main():
  test_modules()
  
  
def test_modules():
  v = sys.version_info
  p = sys.platform
  n = os.name
  env_path = os.getenv('PATH')
  curr_work_dir = os.getcwd() # get current working directory
  os_r_b = os.urandom(25) # operation system returns a random number generator 25 bytes long in bytes
  os_r_h =os.urandom(25).hex() # operation system returns a random number generator 25 bytes long in hexadecimal
  r_i = random.randint(1,100) # random int number between 1 and 1000
  l = list(range(25))
  now = datetime.datetime.now()
  
  print('Python version {}.{}.{}'.format(*v))
  print(p)
  print(n)
  print(env_path)
  print(curr_work_dir)
  print(os_r_b)
  print(os_r_h)
  print(r_i)
  print(l)
  random.shuffle(l)  # random shuffles a list
  print(l)
  print(now)
  print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
  
if __name__=='__main__':main()