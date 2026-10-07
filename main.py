import json
import os
from prettytable import PrettyTable

# Membaca file JSON
with open("barang.json", "r", encoding="utf-8") as data:
    barang = json.load(data)

# Sebelum kembali ke perulangan, def ini akan dipanggil
def freeze():
    input("\nKlik Enter untuk kembali ke menu...")
    os.system("cls" if os.name == "nt" else "clear")

# Menunjukkan barang yang ada didalam JSON
def tabelbarang():
    tabel = PrettyTable()
    tabel.field_names = ("Barang", "Stok")
    for i in barang:
        tabel.add_row([i["barang"], i["stok"]])
        print(tabel)
    freeze()

# Menambahkan barang ke JSON
def nambah():
    nama = input("Masukkan nama barang: ")
    stok = input("Masukkan stok: ")
    barang.append({"barang": nama, "stok": stok})

    with open("barang.json", "w", encoding="utf-8") as data:
        json.dump(barang, data, indent=4)
        print(f"Barang {nama} berhasil ditambah dengan stok {stok}.")
    freeze()

# Menu
def main():
    while True:
        print("========== PROGRAM INPUT BARANG ==========")
        print("1: Lihat barang")
        print("2: Menambahkan barang")
        print("0: Keluar")
        selection = input("Pilihan: ")
        
        if selection == "1":
            tabelbarang()

        elif selection == "2":
            nambah()
        
        elif selection == "0":
            print("Terimakasih")
            break

        else:
            print("Tidak valid")
            freeze()

main()