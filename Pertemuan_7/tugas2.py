#pemesanan restoran

nama=input("Masukan Nama : ")
hp=input("Masukan No HP : ")
menu=str(input("Mau pesan apa?(makanan/minuman) : "))
if menu == "makanan":
    print("""
==============================
List Menu makanan
==============================
A. Nasi Goreng : Rp. 15.000
B. Mie Goreng : Rp 12.000
C. Ayam Geprek : Rp 18.000
""")

elif menu == "minuman":
    print("""
==============================
List Menu Minuman Kopi 
==============================
D. Aneka Jus: Rp 11.000
E. Soft Drink: Rp 12.000
F. Sweet Ice Tea : Rp 11.000

==============================
""")
pesan=input("Mau pesan apa?(masukkan list abjad sesuai menu) : ")
Jp=int(input("Masukkan jumlah pesanan : "))
if pesan == "A":
        listmenu= "Nasi Goreng"
        Th=(15000*Jp)
elif pesan == "B":
        listmenu= "Mie Goreng"
        Th=(12000*Jp)
elif pesan == "C":
        listmenu= "Ayam Geprek"
        Th=(18000*Jp)
elif pesan == "D":
        listmenu= "Aneka Jus"
        Th=(11000*Jp)
elif pesan == "E":
        listmenu= "Soft Drink"
        Th=(12000*Jp)
elif pesan == "F":
        listmenu= "Sweet Ice Tea"
        Th=(11000*Jp)


print("Nama  :",nama)
print("No HP  :",hp)
print("Menu :",listmenu)
print("Jumlah Pesan :",Jp)
print("--------------------------")
print("Jumlah Bayar :",Th)
