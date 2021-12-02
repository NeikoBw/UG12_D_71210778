a = int(input("Masukan Tinggi : "))

for x in range(a):
    for y in range(a,x,-1):
        print(" ", end ="")
    for y in range(2*x+1):
        print("*", end ="")
    print()

for x in range(a-2,-1,-1):
    for y in range(a,x,-1):
        print(" ",end ="")
    for y in range(2*x+1):
        print("*", end ="")
    print() 
    for y in range(a,x,-1):
        print(" ", end ="")
    for y in range(2*x+1):
        print("*", end ="")
    print()