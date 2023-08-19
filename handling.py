#Error Handling

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
  print('Geçerli parola:aa try bloğu')
finally:
  print('Validation tamamlandı ')
'''

class Person:
  def __init__(self, name, year):
    if len(name) > 10:
      raise Exception("Name alanı fazla karakter içeriyor az karaktersiz yapın")
    else:
      self.name = name

p = Person("Aliiiiiiiiiiiiiiiiiii", 1999)














