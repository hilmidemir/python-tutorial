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

class Person():
  def __init__(self, fname, lname):
    self.firstName = fname
    self.lastName = lname
    print('Person created')
  def who_am_i(self):
    print('I m a person')
class Student(Person):
  def __int__(self, fname, lname):
    Person.__init__(self, fname, lname)
    print(f'Student Created {fname}')

class Teacher(Person):
  def __init__(self, fname, lname, branch):
    super().__init__(fname, lname)
    self.branch = branch

  def who_am_i(self):
    print(f'i am a {self.branch} teacher')

p1 = Person('Nurşah', 'Bilen')
s1 = Student('Hilmi', 'Demir')
t1 = Teacher('Serkan', 'Yılmaz', 'Matematik')

t1.who_am_i()
print(p1.firstName)

