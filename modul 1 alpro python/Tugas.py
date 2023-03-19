import os
os.system("cls")

def menghitungRata_rata(): 
  """fungsi untuk menghitung nilai rata - rata yang dimasukkan oleh user"""
  jumlah = int (input("Masukkan jumlah angka yang akan di hitung rata-ratanya : "))
  total_nilai = 0
  for x in range (jumlah):
    nilai = int(input("Nilai ke-"+ str(x+1) + ": "))
    total_nilai += nilai

  rata_rata = total_nilai / jumlah
  os.system("cls")
  print("rata - rata dari ", jumlah, "nilai yang dimasukkan adalah : ", rata_rata)

 
def gajih_bersih():
  """fungsi untuk menghitung gajih bersih setelah di potong pajang 5%"""
  nama = input("nama : ")
  tunjangan = int(input("tunjangan : "))
  gajihPokok = int(input("gajih Pokok : "))

  pajak = (5* (tunjangan + gajihPokok))/100
  gajihBersih = (tunjangan + gajihPokok) - pajak
  
  os.system("cls")
  print("============================")
  print("======= GAJIH BARSIH =======")
  print("============================")
  print("NAMA         : ", nama)
  print("TUNJANGAN    : ", tunjangan)
  print("PAJAK        : ", pajak)
  print("GAJIH POKOK  : ", gajihPokok)
  print("GAJIH BERSIH : ", gajihBersih, "\n")

def perulanganFor(nilai):
  for a in range(nilai):
    print(a, end=" ")
  print("\n")

def perulangaWhile(nilai):
  ulang = int (1)
  while ulang < nilai:
    print(ulang, end=" ")
    ulang += 1
  print("\n")


while True:
  print("===== Menu =====")
  print("1. menghitung rata nilai")
  print("2. menghitung gajih bersih")
  print("3. perulangan for")
  print("4. perulangan while")
  print("0. Keluar ")

  pililihan = int(input("Pilihan : "))

  if pililihan == 1:
    menghitungRata_rata()
    continue
  elif pililihan == 2:
    gajih_bersih()
    continue
  elif pililihan == 3:
    nilai = int(input("MASUKKAN JUMLAH PERULANGAN : "))
    perulanganFor(nilai)
    continue
  elif pililihan == 4:
    nilai = int(input("MASUKKAN JUMLAH PENGULANGAN : "))
    perulangaWhile(nilai)
    continue
  elif pililihan == 0:
    print("Anda telah keluar dari program..")
    break
  else:
    print("Pilihan tidak tersedia...")
