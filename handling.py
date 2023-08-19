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









