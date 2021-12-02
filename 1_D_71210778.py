x = int(input("Masukkan awal deret : ")) 
y = int(input("Masukkan akhir deret : "))

if x + 1 % 2 == 0:
    for z in range (x+1, y, 2):
        if z % 3 == 0 or i % 7 == 0:
             continue
        print ( z , end = " " )
else:
    for z in range (x , y , 2):
        if z % 3 == 0 or z % 7 == 0 : 
            continue
        print (z , end = " ")