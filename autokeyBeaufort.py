

def rubahKunci(plaint,key):
    
    if((len(plaint)== len(key)) or (len(plaint)> len(key))):
        
        key = list(key)
        plaintBalik = list(plaint)
        plaintBalik.reverse()
        
        
        
        if len(plaint) == len(key):
            return key
        
        else:
           
            for i in range(len(plaint)-len(key)):
               
                key.append(plaintBalik[i % len(key)])
                
       
        return ("".join(key))
   
    
    else:
       
        key = list(key)
      
        keys = []
        
        
        for i in range(len(plaint)):
            
            keys.append(key[i])
            
      
    return ("".join(keys))

def enkripsiVignere(plaint,key):
    cipher_text = []
    for i in range(len(plaint)):
        x = ((ord(key[i]) - ord(plaint[i])+256)%256)
        cipher_text.append(chr(x))
    return ("".join(cipher_text))

def dekripsiVignere(cipher,key):
    original_text = []
    for i in range(len(cipher)):
        x = ((ord(key[i]) - ord(cipher[i])+256)%256)
        original_text.append(chr(x))
    return("".join(original_text))
        
    


plaint = 'DIANNUSWANTORO'
key = 'POLKE'
cipher = rubahKunci(plaint,key)
print(cipher)
enkripsi_autokeyBeauforth = enkripsiVignere(plaint,cipher)
print(enkripsi_autokeyBeauforth)
deskripsi_autokeyBeauforth = dekripsiVignere(enkripsi_autokeyBeauforth,cipher)
print(deskripsi_autokeyBeauforth)

