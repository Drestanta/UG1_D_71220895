#diamond
angka = int(input('Masukkan angka : '))
print()
  
for i in range(angka):
  print(' ' * (angka-i),end='')
  print('* ' * (i+1))
   
for i in range(1,angka):
  print(' ' * (i+1),end='')
  print('* ' * (angka-i))