meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "Bir şakaya karşılık cevap",
            "SHEESH": "Onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "Agresifleşmek/sinirlenmek",
            }

word =input("Merhaba. Sözlüğümüe hoşgeldiniz")

if word in meme_dict.keys():
    print(meme_dict[word])

else:
    print("Bu kelime daha eklenmedi")
