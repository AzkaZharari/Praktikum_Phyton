#menghitung nilai

nama = input("masukkan nama ?")
kelas = input("masukkan kelas ?")
nilai = int(input("masukkan nilai (max = 100) ?"))


print("nama kamu adalah", nama)
print("kelas kamu adalah", kelas)
print("nilai kamu adalah", nilai)
if(nilai > 89 and nilai < 101):
    print("istimewa")
elif(nilai > 69 and nilai < 90):
    print("sangat bagus")
elif(nilai > 59 and nilai < 70):
    print("cukup")
else:
    print("gagal")