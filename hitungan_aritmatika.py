from aritmatika_modul import *
from bangun_datar import *
from bangun_ruang import *
from hitungan_aritmatika import *

def menu():
        while True:
                print("pilih program yaa")
                print("1. aritmatika")
                print("2. bangun datar")
                print("3. bangun ruang")
                print("4. keluar")

                pilihan = float(input("masukkan pilihan: "))

                if pilihan == 1:
                        hitungan_aritmatika()
                elif pilihan == 2:
                        bangun_datar()
                elif pilihan == 3:
                        bangun_ruang()
                elif pilihan == 4:
                        break
                else:
                        print("pilihan tidak ada")

def hitungan_aritmatika():
        print("/npilih operasi aritmatika yang ingin dilakukan:")
        print("1. penambahan")
        print("2. pengurangan")
        print("3. perkalian")
        print("4. pembagian")
        print("5. pangkat")
        pilihan = int(input("\nmasukkan nomor operasi aritmatika yang dipilih (1,5):"))

        if pilihan == 1:
                a = float(input("masukkan angka pertama:"))
                b = float(input("masukkan angka kedua:"))
                print("hasil penambahan:", tambah(a,b))
        elif pilihan == 2:
                a = float(input("masukkan angka pertama:"))
                b = float(input("masukkan angka kedua:"))
                print("hasil pengurangan:", kurang(a,b))
        elif pilihan == 3:
                a = float(input("masukkan angka pertama:"))
                b = float(input("masukkan angka kedua:"))
                print("hasil perkalian:", kali(a,b))
        elif pilihan == 4:
                a = float(input("masukkan angka pembilang:"))
                b = float(input("masukkan angka penyebut(tidak boleh nol):"))
                print("hasil pembagian:", bagi(a,b))
        elif pilihan == 5:
                a = float(input("masukkan angka dasar:"))
                b = float(input("masukkan angka pangkat:"))
                print("hasil eksponensial:", pangkat(a,b))
        else:
                print("pilihan tidak valid.")

def bangun_datar():
        print("pilih bangun datar yang ingin dihitung:")
        print("1. lingkaran")
        print("2. persegi")
        print("3. segitiga")
        print("4. trapesium")
        print("5. jajar genjang")
        pilihan = int(input("\nmasukkan nomor bangun datar yang dipilih"))
        if pilihan == 1:
                r = float(input("masukkan jari-jari:"))
                print("luas lingkaran:", luas_lingkaran(r))
        elif pilihan == 2:
                s = float(input("masukkan sisi:"))
                print("luas persegi:", luas_persegi(s))
        elif pilihan == 3:
                a = float(input("masukkan alas:"))
                t = float(input("masukkan tinggi:"))
                print("luas segitiga:", luas_segitiga(a,t))
        elif pilihan == 4:
                p = float(input("masukkan panjang sisi 1:"))
                t = float(input("masukkan tinggi sisi 2:"))
                print("luass persegi panjang", luas_persegi_panjang(p,t))
        elif pilihan == 5:
                a = float(input("masukkan alas:"))
                t = float(input("masukkan tinggi:"))
                print("luas jajar genjang:", luas_jajar_genjang(a,t))
        else :
                print("pilihan tidak valid")

def bangun_ruang():
        print("pilih bangun ruang yang ingin dihitung:")
        print("1. balok")
        print("2. kerucut")
        print("3. tabung")
        print("4. bola")
        print("5. kubus")
        pilihan = int(input("\nmasukkan nomor bangun ruang yang dipilih"))
        if pilihan == 1:
                p = float(input("masukkan panjang:"))
                l = float(input("masukkan lebar:"))
                t = float(input("masukkan tinggi:"))
                print("luas permukaan balok:", luas_permukaan_balok(p,l,t))
        elif pilihan == 2:
                r = float(input("masukkan jari-jari:"))
                t = float(input("masukkan tinggi:"))
                print("luas permukaan kerucut:", luas_permukaan_kerucut(r,t))
        elif pilihan == 3:
                r = float(input("masukkan jari-jari:"))
                t = float(input("masukkan tinggi:"))
                print("luas permukaan tabung:", luas_permukaan_tabung(r,t))
        elif pilihan == 4:
                r = float(input("masukkan jari-jari:"))
                print("luas permukaan bola:", luas_permukaan_bola(r))
        elif pilihan == 5:
                s = float(input("masukkan sisi:"))
                print("luas permukaan kubus:", luas_permukaan_kubus(s))
        else:
                print("pilihan tidak valid")


if __name__ == "__main__":
        menu()