'''
name = input('Lütfen adınızı giriniz: ')
age = int(input('Lütfen yaşınızı giriniz: '))
education = input('Lütfen eğitin durumunuzu (lise, ortaokul, üniversite olarak) giriniz: ')
if (age < 18) :
  print('')
  if (education == 'lise' or education == 'üniversite') :
    print(f'Tebrikler {name} ehliyet almaya hak kazandınız.')
  else:
    print('Ehliyet almak için eğitim durumunuz yetersiz')
else:
  print('Yaşınız ehliyet almaya uygun değildir')
'''
'''
yazili1 = int(input('1. yazılı '))
yazili2 = int(input('2. yazılı '))
sozlu = int(input('sözlü notu '))

ort = (yazili2 + yazili1 +sozlu) / 3

if (ort >= 0) and (ort < 25):
  print('Notunuz 0')
elif (ort >= 25) and (ort < 45):
  print("notunuz 1")
elif (ort >= 45) and (ort < 55):
  print("notunuz 2")
elif (ort >= 55) and (ort < 70):
  print("notunuz 3")
elif (ort >= 70) and (ort < 85):
  print("notunuz 4")
else:
  print("notunuz 5")
'''
'''
import datetime

input_date_str = input('Aracın trafiğe çıkış tarihini giriniz ör:(07/08/2022): ')
input_date_str.split('/')
trafigeCikis = datetime.datetime(int(input_date_str[0]), int(input_date_str[1]), int(input_date_str[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days <= 365:
  print('1. servis aralığı')
if days <= 365 * 2:
  print('2. servis aralığı')
if days <= 365 * 3:
  print('3. servis aralığı')
'''



























