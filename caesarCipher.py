def enkripsi(plain,geser):
    hasil = " "
    #ulangi variabel a sepanjang kata dari plain
    for a in range(len(plain)):
        # memisah menjadi satu huruf"
        char = plain[a]
        #rubah jadi ascii kemudian terapkan kunci
        #rubah kembali menjadi huruf
        hasil += chr((ord(char)+geser)%256)
        
    return hasil
        
   
def deskripsi(cipher,geser):
    hasil = " "
    #ulangi variabel a sepanjang kata dari plain
    for a in range(len(cipher)):
         # memisah menjadi satu huruf"
        char = cipher[a]
        #rubah jadi ascii kemudian terapkan kunci
        #rubah kembali menjadi huruf
        hasil += chr((ord(char)-geser)%256)
    return hasil


#plain teks
plain = 'aaa'
geser = 3

print(enkripsi(plain,geser))
print(deskripsi('ddd',3))



    

