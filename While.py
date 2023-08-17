'''
numbers = [1, 3, 5, 7, 9, 12, 19, 20]
index = 0

while len(numbers) > index:
  print(numbers[index])
  index += 1

start = int(input('Başlangıç değeri giriniz... '))
end = int(input('bitiş değeri giriniz... '))

while start < end:
  if (start % 2 == 1):
    print(start)
  start += 1

products = {}
productCount = int(input('Ürün sayısını giriniz'))

while productCount > 0:
  productName = input('Ürün adı giriniz: ')
  productPrice = int(input('Ürün fiyatını giriniz: '))
  products.update({'name': productName, 'price': productPrice})
  productCount -= 1
print(products)
'''