#menghitung jarak

kendaraan = input ('''Masukkan nama kendaraan ? (mobil/motor)
jawabanmu =''')
bensin = input ('''Masukkan jenis bensin ? ( pertalite/pertamax/turbo)
jawabanmu =''')


if bensin.lower() == "pertalite" :
     hargabensin = 10000
     jarakbensin = 12
elif bensin.lower() == "pertamax" :
     hargabensin = 14000
     jarakbensin = 13
elif bensin.lower() == "turbo" :
     hargabensin = 17000
     jarakbensin = 13,5 
else :
    print('Data bensin tidak ada')
    exit()

kota = input ('''Masukkan kota yang di tuju ? (Jakarta/Depok/Bekasi/Tangerang/Bogor)
jawabanmu =''')

if kota.lower() == "jakarta" :
    jarakkota = 20
elif kota.lower() == "bekasi" :
    jarakkota = 35.7
elif kota.lower() == "depok" :
    jarakkota = 5
elif kota.lower() == "tangerang" :
    jarakkota = 99
elif kota.lower() == "bogor" :
    jarakkota = 120.6
else :
    print('Data bensin tidak ada')
    exit()


pemakaianbensin = jarakkota / jarakbensin
pemakaianperliter = pemakaianbensin * hargabensin
print("Kendaraan kamu adalah", kendaraan.upper())
print("Jenis bensin kamu adalah", bensin.upper())
print("Kota yang kamu tuju adalah", kota.upper())
print("Pemakaian bensin", "{:.2f}".format (pemakaianbensin), "liter")
print("Total harga dari bensin yang dikeluarkan ? Rp.", int (pemakaianperliter))
