#Biodata Diri

def biodata_diri(nama,alamat,ttl,umur,tinggibadan):

    print('================================')

    print('Biodata anda adalah: ')
    print('Nama : ' + nama)
    print('Alamat : ' + alamat)
    print('TTL : ' + ttl)
    print('Umur : ' + umur)
    print('Tinggi badan : ' + tinggibadan)\
    
    beratbadanideal = int(tinggibadan) - 110
    print('Berat badan ideal : ', beratbadanideal)
    
    print('================================')

biodata_diri("Azka Zharari", "Pasir Putih, Sawangan", "Jakarta, 20 Februari 2004", "18 Tahun", "170")

