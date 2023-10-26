
def rubahKunci(plaint,key):
    
    if((len(plaint)== len(key)) or (len(plaint)> len(key))):
         #pisah string menjadi char dalam bentuk list
        key = list(key)
    
        #cek apakah panjang kata dari plainteks sama dengan kunci
        if len(plaint) == len(key):
            return key
        #jika tidak sama maka
        else:
            #ulangi variabel i sampai panjang plain - panjang key
            for i in range(len(plaint)-len(key)):
                #masukan ke dalam list key index ke i di modulo panjang key 
                key.append(key[i % len(key)])
                
        #gabungkan jadi satu
        return ("".join(key))
   
    # jika plaint lebih kecil dibanding key
    else:
        # pecah menjadi list key 
        key = list(key)
        # siapkan wadah keys baru
        keys = []
        #ulangi i sebanyak panjang dari teks plain
        for i in range(len(plaint)):
            #masukan kedalam keys isian dari key dengan indeks ke i
            keys.append(key[i])
            
    #gabungkan jadi satu dengan keys        
    return ("".join(keys))
            
        
        
def enkripsiVignere(plaint,key):
    cipher_text = []
    for i in range(len(plaint)):
        x = (ord(plaint[i]) + ord(key[i])%256)
        cipher_text.append(chr(x))
    return ("".join(cipher_text))

def dekripsiVignere(cipher,key):
    original_text = []
    for i in range(len(cipher)):
        x = (ord(cipher[i]) - ord(key[i])%256)
        original_text.append(chr(x))
    return("".join(original_text))
    
        
        

plaint = 'POLKE'
key = 'DIANNUSWANTORO'
cipher = rubahKunci(plaint,key)

enkripsi_Vignere = enkripsiVignere(plaint,cipher)

deskripsi_Vignere = dekripsiVignere(enkripsi_Vignere,cipher)
print(deskripsi_Vignere)

