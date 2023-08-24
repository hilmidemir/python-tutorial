'''
def my_decorator(func):
  def wrapper():
    print("Fonksiyondan önceki işlemler")
    func()
    print("Fonksiyondan sonraki işlemler")
  return wrapper

@my_decorator
def sayHello():
  print("hello")

sayHello()
'''

import math
import time

def calculate_time(func):
  def inner(*args, **kwargs):
    start = time.time()
    time.sleep(1)
    func(*args, **kwargs)
    finish = time.time()
    print("Fonksiyon " + func.__name__   + str(finish - start) + 'saniye sürdü.')
  return inner

@calculate_time
def usAlma(a,b):
  print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
  print(math.factorial(num))

usAlma(2,3)