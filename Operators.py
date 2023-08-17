# Assigments
'''
# x = 5
# y = 10
# z = 20

x, y, z = 5, 10, 15

# x, y = y, x    x ve y değerleri değişir

values = 1, 2, 3, 4 ,5
print(values)
print(type(values))
x, y, *z = values  # eğer tuplemiz içinde az veya fazla eleman varsa atama yapamayız
print(x, y, z)
print(x,y ,z[2])
'''
'''
x, y, z = 2, 5,10
numbers = 1,5,7,10,6

# num1 = int(input("1. sayı"))
# num2 = int(input("2. sayı"))          #kullanıcıdan alınan iki sayının çarpımından x y z toplamını çıkarma
# result = (num1 * num2) - (x + y +z )

#result = y // x  # y nin x e kalansız bölümü

print(result)
'''

# comperasion operators
'''
username = "hilmi"
a, b, c,d = 5,5,10,4

result = (a== b) #True
result = (a== c) #False
result = ('eşşek' != username)
'''
# ----------------------------------------------------------------

# Logical Operators
'''
x = 5
hak = 5
devam = 'e'
result = 5 < x <10

#and
result = (x > 5) and (x<10)  #true, true => true
result  = (hak > 0) and (devam == 'e')

#or
result = (x> 0 ) or (x%2 == 0)  #true, false => true
result = (x< 0 ) or (x%2 == 0)  #false, false => false

#not
result = not(x>0)  #false

#x, 5-10 arasında olan çift bir sayı mıdır?
result = ((x>5) or (x<10) and (x%2 == 1))

print(result)
'''
# -----------------------------------------------------

# Identity Operator: is

x = y = [1,2,3]
z = [1,2,3]

# print(x == y)
# print(x == z) # true
# print(x is y) # true
# print(x is z) #false
# print(x is not z) # trueeee

# membership operatior: im

x = ['apple', 'banana']
print('banana' in x) # true

name = 'nurşah'
print('a' in name)
print('a' not in name)


















