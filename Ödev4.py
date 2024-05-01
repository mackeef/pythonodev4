import sqlite3
import Levenshtein
import os

# SQLite veritabanını oluştur
conn = sqlite3.connect("texts.db")
c = conn.cursor()

# Text tablosunu oluştur
c.execute("""
    CREATE TABLE IF NOT EXISTS Texts (
        id INTEGER PRIMARY KEY,
        text_content TEXT
    )
""")

# Kullanıcıdan iki metin al
text1 = input("İlk metni girin: ")
text2 = input("İkinci metni girin: ")

# Metinleri veritabanına ekle
c.execute("INSERT INTO Texts (text_content) VALUES (?)", (text1,))
c.execute("INSERT INTO Texts (text_content) VALUES (?)", (text2,))

# Değişiklikleri kaydet
conn.commit()

# Levenshtein mesafesi ile benzerlik oranını hesapla
lev_distance = Levenshtein.distance(text1, text2)
max_len = max(len(text1), len(text2))
similarity_ratio = (1 - lev_distance / max_len) * 100

# Benzerlik oranını ekrana yazdır
print(f"Benzerlik oranı: {similarity_ratio:.2f}%")

# Benzerlik durumu hakkında rapor oluştur
report = f"İlk metin: {text1}\nİkinci metin: {text2}\nBenzerlik oranı: {similarity_ratio:.2f}%\n"

# Raporu 'benzerlik_durumu.txt' dosyasına yazdır
with open("benzerlik_durumu.txt", "w") as f:
    f.write(report)

# Bağlantıyı kapat
conn.close()

print("Benzerlik durumu 'benzerlik_durumu.txt' dosyasına yazıldı.")
