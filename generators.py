'''
import time

def calculate_time(func):
  def inner(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    finish = time.time()
    print("Fonksiyon " + func.__name__   + str(finish - start) + 'saniye sürdü.')
    return result
  return inner

@calculate_time
'''

'''
def cube():
  for i in range(999):
    yield i ** 3

iterator = cube()
# iterator = iter(generator)
for i in iterator:
  print(i)
'''

generator = (i**3 for i in range(5))
print(generator)

for i in generator:
  print(i)




















