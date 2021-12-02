Matkul = [
    ["1 Algoritma Graf", "3 Sistem Operasi", "4 PAK"], #senin
    ["2 Matematika Teknik", "4 Bhs Indonesia", "6 PKN"], #selasa
    ["2 Sistem Basis Data", "4 Praktikum Sistem Basis Data"], #rabu  
    ["1 IMK", "3 LogMat", "4 Praktekkom"], #kamis  

    ]

while True:
    pilihan = str(input("Hi Kiko, Silahkan Masukkan hari yang ingin Anda telusuri: ")).upper() 

    if pilihan == "SENIN" :
        for x in Matkul [0]:
            print("Kelas ke-",format(x))
    elif pilihan == "SELASA" :
        for x in Matkul [1]:
            print("Kelas ke-",format(x))
    elif pilihan == "RABU" :
        for x in Matkul [2]:
            print("Kelas ke-",format(x))
    elif pilihan == "KAMIS" :
        for x in Matkul [3]:
            print("Kelas ke-",format(x))
    elif pilihan == "JUMAT" :
        print("Hari", pilihan, "Anda tidak ada kelas")
    
    break