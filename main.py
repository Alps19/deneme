meme_dict = {
    "LOL": "komik bir şeye verilen cevap",
    "CRINGE": "garip ya da utandırıcı bir şey",
    "ROFL": "bir şakaya karşılık cevap",
    "SHEESH": "onaylamamak",
    "CREEPY": "korkunç",
    "AGGRO": "agresifleşmek/sinirlenmek"
    }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    
if word in meme_dict.keys():
    print(meme_dict[word])
else:
     print("Geçersiz bir kelime girdiniz. Lütfen listeden bir kelime seçin.")
