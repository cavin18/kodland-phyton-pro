memedictionary = {"CRINGE": "Sesuatu yang sangat aneh atau memalukan", 
                  "LOL": "Tanggapan umum terhadap sesuatu yang lucu", 
                  "ROFL": "Tanggapan terhadap lelucon"}

word = input("Halo, Selamat datang di Kamus Meme, silahkan ketik kata yang tidak kamu mengerti (gunakan huruf kapital semua!): ")

if word in memedictionary.keys():
    print(memedictionary[word])
else:
    print("Maaf kata yang anda cari sepertinya tidak ada dalam kamus kami :<")
