#lab praktikum

kondisi = input("masukkan kondisi lab(tersedia/penuh/tidak ada) ?")

if(kondisi == "tersedia"):
    print("jadi praktikum")
elif(kondisi == "penuh"):
    print("pindah jadwal")
elif(kondisi == "tidak ada"):
    print("tidak jadi praktikum")
else:
    print(error)