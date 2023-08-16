''''
type casting
x = input("1. Number: ")
type(x)
y = input("2. Number: ")
type(y)

total = int(x) + int(y)

print(total)
'''

# --------------------------------------------------

#character arrays

name = 'hilmi'
surname = 'demir'
age = 31

greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old.'

#print(greeting)
#print(greeting[1])
#print(len(greeting))
#print(greeting[-1])    This is for use last word of string
#print(greeting[-3])
#print(greeting[1:4])   This finds letters from index 1 to index 4
#print(greeting[1:])    This finds letters from index 1 to end
# print(greeting[1:4:2]) This finds one of every 2 letters from index 1 to index 4

# -------------------------------------------------------

# string formats

# print('My name is {} {} and ı m {} years old'.format(name, surname, age))
# print('My name is {0} {1} and ı m {2} years old'.format(name, surname, age))
# print('My name is {s} {n} and ı m {a} years old'.format(n = name, s = surname, a = age))
# print('My name is {s} {n} and ı m {a} years old'.format(n = name, s = surname, a = age))

result = 200 / 700
# print('the result is {r:1.3}'.format(r = result)) second parameter for numbers after comma

# print(f'My name is {name} {surname} and ı m {age} years old'.format(name, surname, age))

# ---------------------------------------------------------
# string methods

message = 'you shall not pass'

# message.upper() #all words are upper case now
# message.lower() all words are lower case now
# message.title() all words first letter upper case
# message.capitalize() only first word's first letter is lower case
# message.strip() eğer mesaj boşlukla başlıyorsa boşkul silinir
# message.split() split metodu işte amk ama içine parametre verirsek ona göre böler /aynı k*rt gibi
# message = ' '.join(message) split methoduyla ayrılmış dizinin içindeki elemanları boşluk bırakarak geri birleştirir
# isFound = message.startswith('y') mesajın y harfi ile mi başladığını kontrol eder
# isFound = message.endsswith('s') mesajın s harfi ile mi bittiğini kontrol eder

# message = message.replace('you', 'cunt')
# message = message.replace('ç', 'c')

# message = message.center(50,'.')
# print(message)

#-------------------------------------------------------

#Lists

brands = ['BMW', 'Mercedes', 'Audi', 'Mazda']
#print(brands)
#print(len(brands))
#brands[-1] = 'Ferrari'
#print(brands[:3])
#brands[2:] = ['Toyota', 'Renault']   3. ve 4. elemanın değerini değişir
#brands2 = ['Pagani', 'Nissan']
#brands = brands + brands2
#print(brands)
#brands.pop(-1)                 Son elemanı siler
#print(brands)
#print(brands[::-1]           Listeyi tersten yazar

#-------------------------------------------------------------------

#List methods

numbers = [1, 4, 7, 8, 6, 1, 9]
letters = ['a', 'f', 't', 'b', 'r', 'n']

#numbers.append(31)
#numbers.append(52)
#numbers.insert(3, 31) 3. indexten sonra 31 sayısını ekledik
#numbers.pop() son elemanı siler içine verdiğimiz parmetredeki elemanı da silebiliriz       Bunların hepsini Letters için de yapabiliriz
#numbers.remove() içine yazılan değeri bulur ve siler
#numbers.sort()  listeyi sıralamamızı sağlar
#numbers.reverse()  listeyi terse çevirmemizi sağlar
#numbers.count(1) listenin içinde 1 sayısının kaç adet olduğunu söyler

names = ['Ali', 'Yağmur', 'Hasan', 'Deniz']
years = [1998, 2000, 1998, 1987]

#names.append('Cenk tosun sana kosun')
#names.insert(0, 'Sena') Listenin başına sena ekledik
#names.remove('Deniz')
#print(names.index('Deniz')) Deniz kelimesinin indexini gösterir
#isExist = 'Ali' in names     Ali kelimesinin listede olup olmadığını kontrol ediyoruz
#print(isExist)
#print(names.count('Ali'))
#print(names)

#str = "Chevrolet,Dacia"
#str = str.split(',')
#print(str)

#brand1 = input('1. Markayı giriniz')
#brand2 = input('2. Markayı giriniz')
#brand3 = input('3. Markayı giriniz')
#userBrands = []
#userBrands.append(brand1)
#userBrands.append(brand2)
#userBrands.append(brand3)
#print(userBrands)

#--------------------------------------------------------------
'''
Dicktionary

plates = {'Ordu': 52, 'Elazığ': 23, 'Sakarya': 54} Dictionary

plates['Ankara'] = 6
plates['Sakarya'] = 3131

print(plates)
'''

'''
users = {
    'hilmidemir' : {
        'age': 23,
        'address': 'Samsun',
        'roles': ['user']
    },
    'nursahdemir' : {
        'age': 23,
        'address': 'Elazığ',
        'roles': ['admin', 'user']
    }
}
print(users['nursahdemir']['roles'][0])
'''

'''
students = {}

number = input('Öğrenci no: ')
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı ")
phone = input("öğrenci telefon: ")

students.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

number = input('Öğrenci no: ')
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı ")
phone = input("öğrenci telefon: ")

students.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

number = input('Öğrenci no: ')
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı ")
phone = input("öğrenci telefon: ")

students.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})
print('-' * 50)

stdNo = input('Öğrenci No: ')
student = students[stdNo]

print(f'Aradığınız {stdNo} numaralı öğrencinin adı: {student["ad"]} soyadı: {student["soyad"]} ne telefon numarası: {student["telefon"]}dır')

'''









