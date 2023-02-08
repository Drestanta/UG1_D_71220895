# # test case 1
# print("Pilihan Model Matematika")
# print("1. Perkalian")
# print("2. Pembagian")
# kalian = int(input("Masukkan model matematika yang diinginkan 1/2 : "))
# angka = int(input("Menampilkan table matematika dari angka: "))

# if kalian == 1:
#     for kalian in range(1,11):
#         print(angka, "x", kalian, "=", angka*kalian) 
# elif kalian == 2:
#     for kalian in range(50,66):
#         print(kalian, ":", angka, "=", kalian/angka)
# else: 
#     print("Pilihan tidak tersedia, jangan ngasal!")

print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
kalian = int(input("Masukkan model matematika yang diinginkan 1/2 : "))
angka = int(input("Menampilkan table matematika dari angka: "))

if kalian == 1:
    for kalian in range(1,11):
        print(angka, "x", kalian, "=", angka*kalian) 
elif kalian == 2:
    for kalian in range(50,66):
        print(kalian, ":", angka, "=", kalian/angka)
else:
    print("Pilihan tidak tersedia, jangan ngasal!")
