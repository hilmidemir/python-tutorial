'''
#dosya işlemleri: usage open(dosya_adi, dosya_erişme_modu)
#dosya erişme modu dosyayı hangi amaçla açtığımızı belirler.
# w: yazma(yoksa dosya oluşturur) # Var olan bilgileri silip üzerine yazar

#file = open('newFile.txt', 'w', encoding='UTF-8')
#file.write('Hilmi Demir')
#file.close()

# a:append(dosya konumda yoksa oluşturur)

#file = open('newFile.txt', 'a', encoding='UTF-8')
#file.write('Hilmi Demir \n')
#file.close()

# x: create(dosya oluşturur varsa hata verir) #

file = open('newFile2.txt', 'x', encoding='UTF-8')

# r: okuma(dosya yoksa hata verir)
'''
'''
try:
  file = open('newFile.txt', 'r', 'encoding=utf-8')
except FileNotFoundError:
  print('Dosya okuma hatası')
finally:
  print('Dosya kapandı')
  file.close()
'''

'''
file = open('newFile.txt', 'r', encoding='utf-8')
for i in file:
  print(i, end="")
file.close()

file = open('newFile.txt', 'r', encoding='utf-8')
content1 = file.read()
#print(content1)

print('content 2')
file = open('newFile.txt', 'r', encoding='utf-8')
content2 = file.read(5) # Read diyip sonrasında parametre girersek girdiğimiz değer kadar harf okur.
content3 = file.read(3) # İkinci read komutunda ise ilkinde nerde kaldıysa dosyayı tekrar açmadığımız surette kaldığu yerden okumaya devam eder.
print(content2)
print(content3)
file.close()
'''
'''  
file = open('newFile.txt', 'r', encoding='utf-8')

print(file.readline(), end="")
print(file.readline(), end="") # Satır satır okuma işlemi yapar sonuna end ile boş string eklediğimizde bir sonraki readline boş satır olmaz
print(file.readline(), end="")
print(file.readline(), end="")
''' #Readline methodu
'''
file = open('newFile.txt', 'r', encoding='utf-8')
content = file.readlines()
print(content[0])
print(content[1])
print(content[2])
print(content)
'''
'''
with open('newFile.txt', 'r', encoding='utf-8') as file: # with ile açılan dosya kod bloğu bittiğinde kapandığından kendimiz kapatmamız gerekmez
  content = file.read(14) #ilk 10 harfi okur
  print(content)
  file.seek(0) # 0. indexe geri döner ve bir sonraki okumada ordan devam eder.
  print(file.tell())
  content2 = file.read()
  print(content2)
'''
'''
with open('newFile.txt', 'r+', encoding='utf-8') as file: # r+ dediğimizde hem okuma hem de yazma modunda açmış oluyotur
  file.seek(20) # 20. satıra gider ve orada write içine yazdığımız değer kadar silip yerine verdiğimiz şeyleri yazar
  file.write("Burak Evleksiz")

with open('newFile.txt', 'r+', encoding='utf-8') as file: # r+ dediğimizde hem okuma hem de yazma modunda açmış oluyotur
  print(file.read())
'''
'''
with open('newFile.txt', 'a', encoding='utf-8') as file:
  file.write("\nBurak Evleksiz")

with open('newFile.txt', 'r', encoding='utf-8') as file:
  print(file.read())
''' #Sayfa sonuna bilgi ekleme.
'''
with open('newFile.txt', 'r+', encoding='utf-8') as file: # r+ dediğimizde hem okuma hem de yazma modunda açmış oluyotur
  content = file.read()
  content = "Hilmi Demir\n" + content
  file.seek(0)
  file.write(content)
 
with open('newFile.txt', 'r', encoding='utf-8') as file:
  print(file.read()) 
''' #Sayfa başına bilgi ekleme

with open('newFile.txt', 'r+', encoding='utf-8') as file:
  list = file.readlines()
  list.insert(2,'Fenasi Kerim\n')
  file.seek(0)
  #for i in list: file.write(i) #for ile list e attığımız dosya elemanlarını döngüyle tek tek dosyaya yeniden yazıyoruz
  file.writelines(list) # yukarda yaptığımız for oluşturup listeyi tek tek yazmak yerine writelines methodu bunu bizim yerimize yapıyor.

with open('newFile.txt', 'r', encoding='utf-8') as file:
  print(file.read())































