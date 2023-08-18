'''
# Class
class Person:
  # class attributes
  address = 'No information'

  # Constructor(YApıcı method)
  def __init__(self, name, year):
    # Object Attributes
    self.name = name
    self.year = year
    print(f'init methodu çalıştı {name}')

  # Methods
  def intro(self):
    print(f'Hello There {self.name}')


# object (instance)
p1 = Person('Nurşah', 2000)
p2 = Person(year=1999, name='Hilmi')
p1.intro()
''' # Class introduction
'''
# updating
p1.name = 'Nurşah'
p1.address = 'Samsun'
''' # update

'''
print(f'isim: {p1.name}, doğum yılı: {p1.year}, adresi: {p1.address}')
print(f'isim: {p2.name}, doğum yılı: {p2.year}')
''' # accessing object attributes

