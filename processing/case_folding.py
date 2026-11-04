# Fungsi konversi menjadi huruf kecil
def case_folding(query): 
    ALPHABET  = ('A','B','C','D','E','F','G', 'H', 'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    
    hasil = ""
   
    for i in query:
        if i in ALPHABET:
            for k in range(26):
                if i == ALPHABET[k]:
                    hasil = hasil + alphabet[k]
        else:
            hasil = hasil + i

    return hasil