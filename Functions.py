'''
def ekranaYaz(yazi, count):
  for i in range(count):
    print(yazi)
counter = int(input('yazının ekrana kaç kere gösterileceğini yazınız...'))
input = input('Ekrana yazılaca1k yazıyı yazınız... ')
ekranaYaz(input, counter)
'''

'''
def asal_mi(num):
  if num <= 1:
    return False
  elif num <= 3:
    return True
  elif num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True


def asal_bul(num):
  asal_listesi = []
  for i in range(2, num + 1):
    if asal_mi(i):
      asal_listesi.append(i)
  return asal_listesi


sayi = int(input('Asal sayıları bulmak istediğiniz sınırı giriniz: '))
asallar = asal_bul(sayi)
print("Asal sayılar:", asallar)
'''
'''
def bolenler(num):
  bolen = []
  if num == 0:
    print('Sayının böleni yoktur.')
  elif (num > 0) or (num < 0):
    for i in range(2, num):
      if (num % i == 0):
        bolen.append(i)
    if len(bolen) == 0:
      print('Sayının böleni yoktur.')
    else:
      print(bolen)

sayi = int(input('Bölenlerini görmek istediğiniz sayıyı giriniz... '))
bolenler(sayi)
'''























