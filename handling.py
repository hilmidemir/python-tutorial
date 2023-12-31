# Error Handling

'''
try:
  x = int(input('x: '))
  y = int(input('y: '))
  print(x/y)
except ZeroDivisionError:
  print('2. sayı y için 0 girilemez')
except ValueError:
  print('x ve y için girilen değer sayısal olmalıdır.')
'''

'''
while True:
  try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
  except Exception as ex:
    print(f'Yanlış bilgi girdiniz, {ex}')
  else: break
  finally:
    print('try except sonlandı')
'''

'''
def check_password(psw):
  import re
  if len(psw) < 8:
    raise Exception('Parola en az 8 karakterli olmalıdır.')
  elif not re.search("[a-z]", psw):
    raise Exception('Parola küçük harf içermelidir.')
  elif not re.search("[A-Z]", psw):
    raise Exception('Parola büyük harf içermelidir.')
  elif not re.search("[0-9]", psw):
    raise Exception('Parola rakam içermelidir.')
  elif not re.search("[_@$]", psw):
    raise Exception('Parola özel karakter içermelidir.')
  elif re.search("\s", psw):
    raise Exception('Parola boşluk içermemelidir.')
  else:
    print('Geçerli parola')

password = "12345678sB_"

try:
  check_password(password)
except Exception as ex:
  print(ex)
else:
  print('Geçerli parola: try bloğu')
finally:
  print('Validation tamamlandı ')
'''
'''
class Person:
  def __init__(self, name, year):
    if len(name) > 10:
      raise Exception("Name alanı fazla karakter içeriyor az karaktersiz yapın")
    else:
      self.name = name

p = Person("Aliiiiiiii", 1999)
'''
'''
liste = ["1", "2", "5a", "1a1", "31", "52"]

for x in liste:
  try:
    result = int(x)
    print(result)
  except ValueError:
    continue
'''
'''
while True:
  i = input('Bir sayı giriniz çıkmak için q giriniz')
  if i == 'q':
    break
  try:
    i = int(i)
  except ValueError:
    print('Bir sayı giriniz çıkmak için q giriniz')
    continue
'''

'''
def checkPassword(password):
  turkceKarakterler = 'ıüğçöİş'
  for i in password:
    if i in turkceKarakterler:
      raise TypeError('Parolanız türkçe karakter içeremez')
    else:
      pass
  print('Geçerli parola')


password = input('Parola giriniz')
try:
  checkPassword(password)
except TypeError as err:
  print(err)
'''

def faktoriyel(x):
  x = int(x)
  if x < 0:
    raise ValueError('Faktöriyteli alınacak değer 0 dan küçük olamaz')
  result = 1
  for i in range(1, x+1):
    result *= i

  return result

for x in [5, 2, -6,'6a']:
  try:
    y = faktoriyel(x)
  except ValueError as err:
    print(err)
    continue
  print(y)



























