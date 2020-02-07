#!/usr/bin/env python3

from random import random,randint, choice
def main():
  """
  There are two type of decorators: Function Decorator and Class Decorator
  Decorator is a special type of function that returns a wrapper function
  We cannot call f2 directly as it is in scope only inside f1
  It implies 3 conditions:
    1. A function be defined inside another function
    2. A function can be passed as a parameter to another function
    3. A function can return another function  
  A decorator is callable function that is used to modify a function 
  """
  test_decorator()
  test_decorator2()
  
def our_decorator(func):
  def function_wrapper(*args,**kwargs):
    print(f'Before calling {func.__name__}')
    res = func(*args,**kwargs)
    print(res)
    print(f'After calling {func.__name__}')
  return function_wrapper


def foo(x):
  print(f'Hi, foo has been called with {x}')

def test_decorator():
  global foo
  print('We call foo before decoration:')
  foo('Hi')
  print('We now decorate foo with our_decorator:')
  foo=our_decorator(foo)
  print('We call foo after decoration:')
  foo(42)

random = our_decorator(random)
randint = our_decorator(randint)
choice = our_decorator(choice)

def test_decorator2():
  random()
  randint(3,8)
  choice([4,5,6])
  
if __name__=='__main__':main()