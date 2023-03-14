import os
os.system('cls')

# ! ===== operasi di aritmatika =======

# ? operasi membulatkan hasil bagi
x = 20
y = 2
hasil = x // y
print(x,'//',y, '=', hasil)

# ? operasi perpangkatan
hasil = x ** y
print(x,'**',y, '=', hasil)

# ? operasi sisa bagi
hasil = x % y
print(x,'%',y, '=', hasil)

# ! operasi prioritas akan mengeksekusi 
# ? 1. ()
# ? 2. eksponen **
# ? 3. perkalian dan kawan" (* / % //)
# ? 4. pertambahan + -