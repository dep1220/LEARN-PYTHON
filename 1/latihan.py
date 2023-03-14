import os
os.system('cls')
# ! ===== latihan pertama program konversi suhu =====

# print("\n ===== PROGEAM COMPERSI SUHU ====\n")
# celcius = float(input("masukkna suhu yang ingin di kompersi : "))
# print("suhu dalam celcius adalah",celcius,"celcius")

# # todo reamur
# reamur = (4/5)* celcius
# print("suhu dalam reamur adalah",reamur,"reamur")

# # todo fahrenheit
# fahrenheit = (((9/4)*celcius) + 32)
# print("suhu dalam fahrenheit adalah",fahrenheit,"fahrenheit")

# # todo kelvin
# kelvin = celcius + 273
# print("suhu dalam kelvin adalah",kelvin,"kelvin")
print("\n PROGRAM COMPERSI SUHU\n")
fahrenheit = float(input("Masukkan Suhu Fahrenheit yang akan di ubah : "))
kelvin = (fahrenheit + 459.67)* 5/9
print("suhu dalam kelvin adalah : ",kelvin)

kelvin = input("Masukkan Suhu kelvin yang akan di ubah : ")
fahrenheit = kelvin * 9/5 - 459.67
print("suhu dalam fahrenheit : ",fahrenheit)
