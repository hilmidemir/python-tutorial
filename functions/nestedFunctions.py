'''
def autro(num1):
  print("outer")
  def inner_increment(num1):
    print('inner')
    return num1 + 1
  num2 = inner_increment(num1)
  print(num1, num2)

autro(10)
'''  #encapsulation

def factorial(number):
  if not isinstance(number, int):
    raise TypeError('Number must be integer value')
  if not (number >= 0):
    raise ValueError('Number must be greater than 0')
  def innerFactorial(number):
    if number <= 1:
      return 1
    return number * innerFactorial(number - 1)
  return innerFactorial(number)

try:
  print(factorial(-5))
except Exception as ex:
  print(ex)