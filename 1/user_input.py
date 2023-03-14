import os
import time
os.system('cls')
start = time.perf_counter()

# ! ===== episode input user =========
main = int(input("masukkan angka yang pertama : "))
gh = int(input("masukkan angka yang ke dua : "))
print(main + gh);





end = time.perf_counter()
print(start - end)