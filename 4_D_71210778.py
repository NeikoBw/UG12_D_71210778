def nilai_maksimal(x):
  besar = x[0]
  for nilai in x:
    if nilai > besar:
      besar = nilai
  return besar

def nilai_minimal(x):
  kecil = x[0]
  for nilai in x:
    if nilai < kecil:
      kecil = nilai
  return kecil

a = [3, 20, 100, -35, 50]
b = [3, 20, 90, 35, 75]
print(a)
print('Nilai terbesar:', nilai_maksimal(a))
print('Nilai terkecil:', nilai_minimal(a))

print(b)
print('Nilai terbesar:', nilai_maksimal(b))
print('Nilai terkecil:', nilai_minimal(b))
