'''
numbers = [1, 2, 3, 4, 5]

for i  in numbers:
  print(i)

dict = {'k1': 1, 'k2': 2, 'k3': 3}

for k in dict:
  print(k)
'''

'''
numbers = [1, 3, 5, 7, 9, 12, 19, 21]

oddNumbers = []
sq = []
for i in numbers:
  if (i%3 == 0):    # Odd numbers
    oddNumbers.append(i)
    i **= 2
    sq.append(i)

print(f'numbers listesindeki 3 üm katı olan sayılar: {oddNumbers} \nnumbers listesindeki 3 ün katı olan sayıların kareleri: {sq}')

cities = ['Ordu', 'İstanbul', 'Ankara', 'İzmir', 'Samsun']
cit = []
for city in cities:
  if (len(city) > 5):
    cit.append(city)
print(cit)

products = [
  {'name': 'Iphone 11', 'price': '3000'},
  {'name': 'Iphone 12', 'price': '4000'},
  {'name': 'Iphone 13', 'price': '5000'},
  {'name': 'Iphone 14', 'price': '6000'},
  {'name': 'Iphone 15', 'price': '7000'}
]
totalPrice = 0
for product in products:
    totalPrice += int(product['price'])
    if (int(product['price']) > 5000):
      print(product['name'])

print(totalPrice)
'''























