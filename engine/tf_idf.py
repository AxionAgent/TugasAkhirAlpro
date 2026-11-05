# menghitung kemunculan kata disebuah dokumen
def calculate_frequency(token):
    hasil = {}

    for i in token:
        if i in hasil:
            hasil[i] += 1
        else:
            hasil[i] = 1

    return hasil

# menghitung dokumen yang mengandung suatu kata
def calculate_document_frequency(query, stopword):
    hasil = {}

    for i in query:
        hasil[i] = 0
        for k in stopword:
            if i in k:
                hasil[i] += 1

    return hasil

# menghitung seberapa unik dan penting suatu kata
