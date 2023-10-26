a = input("masukan nilai a = ")
b = input("masukan nilai b = ")

#rubah jadi int
c = int(a)
d = int(b)

if (c<0):
    apos = c*-1
    if(c%d == 0):
        hasil = 0
    else:
        hasil = d-(apos%d)
else:
    hasil = c%d

print("hasil a mod b = ", hasil)    