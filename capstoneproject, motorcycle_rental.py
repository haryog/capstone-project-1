# CAPSTONE PROJECT 1 - Rental Motor- 
from datetime import datetime, timedelta
import time
daftar_motor = [
        {
            'plat': 'L 2345 OP',
            'nama': 'Honda',
            'jenis': 'Vario',
            'harga_harian': 80000,
            'kondisi': 'baik',
            'unit' : 'ada',
            'nama_penyewa': '',
            'tanggal_sewa' : '',
            'pengembalian' : '',
        },
        {
            'plat': 'L 1923 WW',
            'nama': 'Yamaha',
            'jenis': 'Nmax',
            'harga_harian': 90000,
            'kondisi': 'dent',
            'unit' : 'ada',
            'nama_penyewa': '',
            'tanggal_sewa' : '',
            'pengembalian' : '',
        },
        {
            'plat': 'L 6758 GG',
            'nama': 'Vespa',
            'jenis': 'Sprint',
            'harga_harian': 80000,
            'kondisi': 'baik',
            'unit': 'ada',
            'nama_penyewa': '',
            'tanggal_sewa' : '',
            'pengembalian' : '',   
        },
    ]
    
def tampil_semuamotor():
    print("\n\t\t============== Data Daftar Motor ==============\n")
    print("No.\t|Plat\t\t\t|Nama Motor\t|Jenis\t\t|Harga Sewa\t\t|Kondisi\t|Unit")
    for i in range(len(daftar_motor)):
        print(f'{i+1}\t|{daftar_motor[i]["plat"]}\t\t|{daftar_motor[i]["nama"]}\t\t|{daftar_motor[i]["jenis"]}\t\t| Rp.{daftar_motor[i]["harga_harian"]}\t\t|{daftar_motor[i]["kondisi"]}\t\t|{daftar_motor[i]["unit"]}')

def tampil_satuanmotor(nama_motor):
    print("No.\t|Plat\t\t\t|Nama Motor\t|Jenis\t\t|Harga Sewa\t\t|Kondisi\t|Unit")
    for i in range(len(daftar_motor)):
        if daftar_motor[i]['nama'] == nama_motor :
            print(f'{i+1}\t|{daftar_motor[i]["plat"]}\t\t|{daftar_motor[i]["nama"]}\t\t|{daftar_motor[i]["jenis"]}\t\t| Rp.{daftar_motor[i]["harga_harian"]}\t\t|{daftar_motor[i]["kondisi"]}\t\t|{daftar_motor[i]["unit"]}')
                 
        
# Sub Menu Tampilkan Stock Motor
def read():
    while True :
        print('''
    [1] Daftar Semua Motor
    [2] Daftar Satuan Motor
    [3] Kembali Ke 'Main Menu'
            ''')
        code_def_read = str(input("Masukan kode [1-3]: "))
        if code_def_read == "1":
            if len(daftar_motor) > 0:
                tampil_semuamotor()
            else:
                print("Tidak ada Daftar Motor, silahkan tambah daftar motor terlebih dahulu")
        elif code_def_read == "2":
            if len(daftar_motor) > 0:
                pilih = input("Masukan Nama Motor yang ingin ditampilkan: ").title()
                present = False
                for i in range(len(daftar_motor)):
                    if pilih == daftar_motor[i]["nama"]: 
                        present = True
                        tampil_satuanmotor(pilih)
                        break
                if present == False:
                    print(" ")
                    print("Data motor tidak ditemukan!, kembali ke menu sebelumnya")
            else:
                print("Tidak ada daftar motor yang ditampilkan, silahkan tambah daftar terlebih dauhulu")
        elif code_def_read == "3":
            mainMenu()
            break
        else :
            print("Input tidak valid. Isi dengan [1-3]")

def tambah_list():
    while True:
            motor_baru = (input("\nMasukan nama motor yang diinginkan: ")).title()
            present = False
            for i in range(len(daftar_motor)):
                if daftar_motor[i]["nama"] == motor_baru:
                    present = True
                    break
            if present == True:
                print(" ")
                print("Data motor sudah tersedia, silahkan kembali lagi ke menu 'Tambah List'")
                create()
                break
            else:
                plat_baru = str(input("\nMasukan plat motor: ")).upper()
                jenis_baru = str(input("\nMasukan jenis motor: "))
                kondisi_baru = str(input("\nMasukan kondisi motor: ")).lower()
                harga_baru = input("\nMasukan harga sewa/hari motor (dalam ribuan): Rp. ")
                if harga_baru.isdigit():
                    unit_baru = "ada"
                    while True:
                        if unit_baru == "ada":
                            print("\nMasukan [1] untuk simpan, [2] untuk batal simpan")
                            code_simpan = str(input("Pilihan: "))
                            if code_simpan == "1":
                                daftar_motor.append(dict(plat = plat_baru, nama = motor_baru, jenis = jenis_baru, harga_harian = harga_baru, kondisi = kondisi_baru, unit = unit_baru))
                                tampil_satuanmotor(motor_baru)
                                print("\nData berhasil disimpan!")
                                create()
                                break
                            elif code_simpan == "2": 
                                print("\nApakah ada perubahan?")
                                print("\n[1] Ya, Kembali ke tambah list, [2] Tidak, Mulai input dari nama lagi") 
                                validasi = input("Pilihan: ")
                                if validasi == "1":
                                    print("\nData tidak disimpan!")
                                    create()
                                elif validasi == "2":
                                    print("\nData tidak disimpan!")
                                    break     
                            else:
                                print("\nInput salah!, Silahkan pilih angka [1/2]")
                else : 
                    print("\nMasukan harga dengan angka!") 
                    tambah_list()  
                             
# Sub Menu Tambah Stock Motor       
def create():
    while True:
        print('''
    [1] Tambah List ke Daftar Motor 
    [2] Kembali Ke 'Main Menu'
            ''')
        code_def_create = str(input("Masukan kode [1-2]: "))
        if code_def_create == "1":
            tambah_list()
            break
        elif code_def_create == "2":
            mainMenu()
            break
        else:
            print("Masukan inputan angka yang sesuai [1/2]")
            create()
            break
        
# Sub-menu Hapus List Stock Motor
def hapus():
    while True:
        print('''
    [1] Hapus Data Motor 
    [2] Kembali Ke Menu Utama
            ''')
        code_def_uptd = str(input("Masukan kode [1/2]: "))
        if code_def_uptd == "1":
            tampil_semuamotor()
            print(" ")
            plat_nomor = str(input("Masukan plat nomor motor yang akan dihapus: ")).upper()
            for i in range(len(daftar_motor)):
                if plat_nomor == daftar_motor[i]['plat']:
                    validasi = input("Apakah anda yakin menghapus data ini (Y/N)? ").upper()
                    if validasi.upper() == "Y":
                        del daftar_motor[i]
                        print("\nData berhasil dihapus!")
                        tampil_semuamotor()
                        hapusDatalagi = input("Apakah anda ingin menghapus data lagi (Y/N)? ").upper()
                        if hapusDatalagi == "Y":
                            hapus()
                            break
                        elif hapusDatalagi == "N":
                            mainMenu()
                    elif validasi == "N":
                        print("\nHapus data dibatalkan!")
                        hapus()
                        break 
                    else:
                        print("Inputan salah, masukan dengan Y/N!")
                        hapus()
                        break
            else:
                print("Masukan plat nomor yang valid!")
        elif code_def_uptd == "2":
            mainMenu()
            break                   
        else:
            print("Masukan inputan angka yang sesuai [1/2]")
            hapus()
            break    
def semua_Tanpaunit():
    print("\n \t\t============== Data Daftar Motor ==============\n")
    print("No.\t|Plat\t\t\t|Nama Motor\t|Jenis\t\t|Harga Sewa\t\t|Kondisi")
    for i in range(len(daftar_motor)):
        print(f'{i+1}\t|{daftar_motor[i]["plat"]}\t\t|{daftar_motor[i]["nama"]}\t\t|{daftar_motor[i]["jenis"]}\t\t| Rp.{daftar_motor[i]["harga_harian"]}\t\t|{daftar_motor[i]["kondisi"]}')

def ganti() :
    while True :
        semua_Tanpaunit()
        plat_nomor = str(input("Masukan plat nomor motor yang akan diupdate: ")).upper()
        not_found = False
        for i in range(len(daftar_motor)):
            if plat_nomor == daftar_motor[i]['plat']:
                not_found = True
                updatean = input("\nData apa yang mau diupdate (isi dengan nama kolom): ")
                if updatean == 'Plat': 
                    update_plat = input("Masukan plat motor yang baru: ").upper()
                    validasi_plat = str(input("Apakah anda yakin update di bagian ini (Y/N)? ")).upper()
                    if validasi_plat == "Y":
                        daftar_motor[i]['plat'] =  update_plat
                        print("\nData Plat berhasil diupdate!")
                        semua_Tanpaunit()
                        update()
                        break
                    elif validasi_plat == "N":
                        print("\nData Plat tidak berhasil diupdate!")
                        ganti()
                        break
                    else:
                        print("Masukan inputan yang benar!")
                        ganti()
                        break
 
                elif updatean == "nama motor" or updatean == "nama": 
                    update_nama = input("Masukan nama motor yang baru: ").capitalize()
                    validasi_nama = str(input("Apakah anda yakin update di bagian ini (Y/N)? ")).upper()
                    if validasi_nama == "Y":
                        daftar_motor[i]['nama'] =  update_nama
                        print("\nData Nama Motor berhasil diupdate!")
                        semua_Tanpaunit()
                        update()
                        break
                    elif validasi_nama == "N":
                        print("\nData Nama Motor tidak berhasil diupdate!")
                        ganti()
                        break
                    else:
                        print("Masukan inputan yang benar!")
                        ganti()
                        break
                        
                elif updatean == "jenis": 
                    update_jenis = input("Masukan jenis motor yang baru: ").capitalize()
                    validasi_jenis = str(input("Apakah anda yakin update di bagian ini (Y/N)? ")).upper()
                    if validasi_jenis == "Y":
                        daftar_motor[i]['jenis'] =  update_jenis
                        print("\nData Jenis berhasil diupdate!")
                        semua_Tanpaunit()
                        update()
                        break
                    elif validasi_jenis == "N":
                        print("\nData Jenis tidak berhasil diupdate!")
                        ganti()
                        break
                    else:
                        print("Masukan inputan yang benar!")
                        ganti()
                        break
                    
                elif updatean == "harga" or updatean == "harga sewa": 
                    update_hargaSewa = input("Masukan harga sewa yang baru (dalam ribuan): Rp. ")
                    if update_hargaSewa.isdigit():
                        validasi_harga = input("Apakah anda yakin update di bagian ini (Y/N)? ").upper()
                        if validasi_harga == "Y":
                            daftar_motor[i]['harga_harian'] =  update_hargaSewa
                            print("\nData Harga Sewa berhasil diupdate!")
                            semua_Tanpaunit()
                            update()
                            break
                        elif validasi_harga == "N":
                            print("\nData Harga Sewa tidak berhasil diupdate!")
                            ganti()
                            break
                        else:
                            print("Masukan inputan yang benar!")
                            ganti()
                            break
                    else:
                        print("\nInput harga baru hanya dengan angka!")
                
                elif updatean == "kondisi": 
                    update_kondisi = input("Masukan kondisi motor yang baru: ").lower()
                    validasi_kondisi = str(input("Apakah anda yakin update di bagian ini (Y/N)? ")).upper()
                    if validasi_kondisi == "Y":
                        daftar_motor[i]['kondisi'] =  update_kondisi
                        print("\nData kondisi Berhasil diupdate!")
                        semua_Tanpaunit()
                        update()
                        break
                    elif validasi_kondisi == "N":
                        print("\nData kondisi tidak berhasil diupdate!")
                        ganti()
                        break
                    else:
                        print("Masukan inputan yang benar!")
                        ganti()
                        break
                else:
                    print("\nKolom yang akan diupdate tidak sesuai!")
                    update()
                    break
        if not_found == False: 
            print("\nData Plat tidak sesuai!")
            update()
            break
        
# Sub-menu Edit List Stock Motor             
def update():
    while True : 
        print('''
    [1] Update Data Motor 
    [2] Kembali Ke Menu Utama
            ''')
        code_def_uptd = input("Masukan kode [1-2]: ")
        if code_def_uptd == "1":
            ganti()
        elif code_def_uptd == "2":
            mainMenu()                
        else:
            print("\nPilihan kode tidak sesuai, Silahkan masukan 1/2!") 
            update()    
                   
def tampil_motorTerental(unit): 
    print("\n \t\t============== Motor Terental ==============\n")
    print("No.\t|Plat\t\t\t|Nama Motor\t|Jenis\t\t|Nama Penyewa\t|Unit\t\t\t|Tanggal Sewa\t\t|Tanggal Pengembalian")
    for i in range(len(daftar_motor)):
        if daftar_motor[i]["unit"] == unit:
            print(f'{i+1}\t|{daftar_motor[i]["plat"]}\t\t|{daftar_motor[i]["nama"]}\t\t|{daftar_motor[i]["jenis"]}\t\t|{daftar_motor[i]["nama_penyewa"]}\t\t|{daftar_motor[i]["unit"]}\t\t|{daftar_motor[i]["tanggal_sewa"]}\t\t|{daftar_motor[i]["pengembalian"]}')

def tampil_tidakTerental(unit): 
    print("\n \t\t============== Data Daftar Motor ==============\n")
    print("No.\t|Plat\t\t\t|Nama Motor\t|Jenis\t\t|Harga Sewa\t\t|Kondisi\t|Unit")
    for i in range(len(daftar_motor)):
        if daftar_motor[i]["unit"] == unit:
            print(f'{i+1}\t|{daftar_motor[i]["plat"]}\t\t|{daftar_motor[i]["nama"]}\t\t|{daftar_motor[i]["jenis"]}\t\t| Rp.{daftar_motor[i]["harga_harian"]}\t\t|{daftar_motor[i]["kondisi"]}\t\t|{daftar_motor[i]["unit"]}')
 

def sewa():
    while True:
        tampil_tidakTerental("ada")
        kode = input("Apakah anda ingin melakukan perentalan Y/N : ").upper()

        if kode == "Y":
            inginRental = input("\nMasukkan plat nomor motor yang akan dirental: ").upper()
            plat_motor_ditemukan = False
            

            for i in range(len(daftar_motor)):
                if inginRental == daftar_motor[i]['plat']:
                    plat_motor_ditemukan = True
                    nama_perental = input("\nNama Perental: ")
                    durasi_sewa = input("\nTotal hari rental motor (input angka saja): ")
                   
                    if durasi_sewa.isdigit():
                        durasi_sewa = int(durasi_sewa)
                        if durasi_sewa <= 7 :
                            tanggal_rental = datetime.now().date()
                            tanggal_pengembalian = tanggal_rental + timedelta(days=int(durasi_sewa))
                            daftar_motor[i]['unit'] = "tidak ada"
                            daftar_motor[i]['nama_penyewa'] = nama_perental
                            daftar_motor[i]['tanggal_sewa'] = tanggal_rental
                            daftar_motor[i]['pengembalian'] = tanggal_pengembalian
                            totalhargaSewa = daftar_motor[i]['harga_harian'] * int(durasi_sewa)
                            print("\nTotal Harga yang harus dibayar adalah")
                            print(f"Rp.{totalhargaSewa}")

                            while True:
                                uang_sewa = input("\nMasukan Uang Untuk Sewa: Rp.")
                                if uang_sewa.isdigit():
                                    kembalian = (int(uang_sewa) - int(totalhargaSewa))

                                    if int(uang_sewa) < totalhargaSewa:
                                        print("\nUang tidak cukup, silahkan input kembali!")
                                    elif int(uang_sewa) > totalhargaSewa:
                                        print(f"\nMotor berhasil disewa!, Kembalian anda Rp.{kembalian}")
                                        rental()
                                        break
                                    else:
                                        print("\nMotor berhasil disewa!")
                                        rental()
                                        break
                                else: 
                                    print("Masukan uang sewa yang sesuai!")
                        else:
                            print("Maximal rental hanya 7 hari saja") 
                    else:
                        print('Masukkan hari rental yang sesuai!')    

            if not plat_motor_ditemukan:
                print('Masukkan plat nomor yang tersedia pada kolom "Plat"')
                continue

        elif kode == "N":
            print("\nKembali ke Menu Rental Motor.")
            break

        else:
            print("\nMasukan Input Y/N!")

    rental()

def pengembalian_rental():
    while True:
        tampil_motorTerental("tidak ada")
        validasi = input("Apakah anda ingin mengembalikan motor Y/N ? ").upper()
        if validasi.upper() == "Y":
            plat_= input("\nMasukan Plat nomor motor yang akan dikembalikan: ").upper()
            for i in range(len(daftar_motor)):
                if plat_ == daftar_motor[i]['plat']:
                    validasi_pengembalian = input("\nApakah anda yakin ingin mengembalikan motor ini (Y/N)? ").upper()
                    if validasi_pengembalian == "Y":
                        daftar_motor[i]['unit'] = 'ada'
                        print("\nMotor berhasil dikembalikan!")
                        rental()
                        break
                    elif validasi_pengembalian == "N":
                        print('\nMotor tidak jadi dikembalikan, kembali ke menu "rental"')
                        rental()
                        break
                    else:
                        print("Masukan input yang benar!")
                        rental()
                        break 
                else :
                    print("Plat tidak ditemukan!")
                    pengembalian_rental()
        elif validasi.upper() == "N":
            print("\nPengembalian tidak berhasil! kembali ke menu rental")
            rental()
            break
        else :
            print("\nInput salah! pilih Y/N")
            pengembalian_rental()
            break

def cek_ketersediaan(daftar_motor):
    while True:
        for i in range(len(daftar_motor)):
            if daftar_motor[i]["unit"] != "ada":
                return False
        else :
            return True
        
# Sub-menu Rental Motor       
def rental():
   while True : 
        print('''
    [1] Daftar Kendaraan Yang Sedang Dirental
    [2] Penyewa Melakukan Rental 
    [3] Pengembalian Rental oleh Penyewa
    [4] Kembali Ke Main Menu  
            ''')
        code_def_rental = input("Masukan kode [1-4]: ")
        if code_def_rental == "1":
            if cek_ketersediaan(daftar_motor):
                print("\nTidak ada motor yang sedang disewa") 
            else:
                tampil_motorTerental("tidak ada")
                rental()
                break
        elif code_def_rental == "2":
            sewa()
            break
        elif code_def_rental == "3":
            if cek_ketersediaan(daftar_motor):
                print("\nTidak ada motor yang sedang disewa")
                rental() 
            else:
                # tampil_motorTerental("tidak ada")
                pengembalian_rental()
            break
        elif code_def_rental == "4":
            mainMenu()
            break
        else:
            print("Kode salah! Masukan [1-4]")
            rental()
            break


def exit_():
    validasi_exit = input("\nApakah anda yakin meninggalkan program Y/N? ").upper()
    if validasi_exit == "Y":
        print("\nSelamat Tinggal, Terimakasih!!!")
        exit()
    elif validasi_exit == "N":
        mainMenu()
    else:
        print('\nInputan salah, anda akan dikembalikan ke "Main menu"')
        mainMenu()
                                 
# Menu Utama
def mainMenu():   
    while True:
        print("")        
        print("====== Rental Motor Jaya =======")
        print(" ")
        print("---------- Main Menu ----------")
        print('''
    [1] Tampilkan Stock Motor
    [2] Tambahkan Stock Motor
    [3] Edit List Stock Motor
    [4] Hapus List Stock Motor
    [5] Rental Motor
    [6] Exit Program
    ''')

        kode = input("Masukan pilihan kode [1-6]: " )
        if kode == "1":
            read() 
            break
        elif kode == "2":
            create()
            break
        elif kode == "3":
            update()
            break
        elif kode == "4":
            hapus()
            break
        elif kode == "5":
            rental()
            break
        elif kode == "6":
            exit_()
            break
        else :
            print("Masukan kode yang sesuai dengan 'Main Menu'")
mainMenu()



        
