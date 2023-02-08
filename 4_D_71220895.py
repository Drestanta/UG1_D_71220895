def pilihan():
    print("-------- Nilai ke 1 --------")
    nilai1 = float(input("Nilai Harian : "))
    uts1 = float(input("Nilai UTS :"))
    uas1 = float(input("Nilai UAS : "))
    nilaiharian = int(nilai1*30/100)
    nilaiuts = int(uts1*30/100)
    nilaiuas = int(uas1*40/100)
    total1 = nilaiharian+nilaiuts+nilaiuas
    print("-------- Nilai ke 2 --------")
    nilai2 = float(input("Nilai Harian : "))
    uts2 = float(input("Nilai UTS :"))
    uas2 = float(input("Nilai UAS : "))
    print("-------- Total Nilai --------")
    nilaiharian2 = int(nilai2*30/100)
    nilaiuts2 = int(uts2*30/100)
    nilaiuas2 = int(uas2*40/100)
    total2 = nilaiharian2+nilaiuts2+nilaiuas2
    total = (total1+total2)/2
    print ("Total nilai yang didapat : ",float(total))
    if total >= 80 :
        print("\nTotal nilai dalam huruf : A")
    elif total >= 60 :
        print("\nTotal nilai dalam huruf : B")
    elif total >= 40 :
        print("\nTotal nilai dalam huruf : C")
    elif total >= 20 :
        print("\nTotal nilai dalam huruf : D")
    elif total >= 0 :
        print("\nTotal nilai dalam huruf : E")

pilihan()