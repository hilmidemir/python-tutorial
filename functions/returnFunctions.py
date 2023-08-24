'''
def usalma(number):
  def inner(power):
    return number ** power
  return inner

two = usalma(2)
three = usalma(3)

print(two(3))
print(three(3))
'''  # kafamı karıştıran o kod
'''
def yetki_sorgula(page):
  def inner(role):
    if role == 'admin':
      return "{0} rolü {1} sayfasına ulaşabilir". format(role, page)
    else:
      return "{0} rolü {1} sayfasına ulaşamaz". format(role, page)
  return inner

user1 = yetki_sorgula("Product Edit")
print(user1('admin')) 
'''  # iç içe fonksiyon kullanımıııı
'''
def islem(islem_adi):
  def toplam(*args):
    toplam = 0
    for i in args:
      toplam += i
    return toplam

  def carpma(*args):
    carpim = 1
    for i in args:
      carpim *= i
    return carpim

  if islem_adi == 'toplama':
    return toplam
  else:
    return carpma

toplama = islem('toplama')
print(toplama(1,5,8,9,6,3,9))

carpim = islem('carp')
print(carpim(3,56,9))
'''  # İç içe fonksiyonların kullanımı

























