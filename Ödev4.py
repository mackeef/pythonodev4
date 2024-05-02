import sqlite3
import Levenshtein
import os

conn = sqlite3.connect("texts.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS Texts (
        id INTEGER PRIMARY KEY,
        text_content TEXT
    )
""")

text1 = input("İlk metni girin: ")
text2 = input("İkinci metni girin: ")

c.execute("INSERT INTO Texts (text_content) VALUES (?)", (text1,))
c.execute("INSERT INTO Texts (text_content) VALUES (?)", (text2,))

conn.commit()

lev_distance = Levenshtein.distance(text1, text2)
max_len = max(len(text1), len(text2))
similarity_ratio = (1 - lev_distance / max_len) * 100

print(f"Benzerlik oranı: {similarity_ratio:.2f}%")

report = f"İlk metin: {text1}\nİkinci metin: {text2}\nBenzerlik oranı: {similarity_ratio:.2f}%\n"

with open("benzerlik_durumu.txt", "w") as f:
    f.write(report)
    
conn.close()

print("Benzerlik durumu 'benzerlik_durumu.txt' dosyasına yazıldı.")
