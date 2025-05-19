import numpy as np


isi_surat = input("Masukkan pesan tersembunyi anda : ")
array_kata = str.split(isi_surat, sep = " ")

kata_tersembunyi = ""
for i in range(0, len(array_kata)):
    kata_tersembunyi += array_kata[i][0]

print("Kata-kata tersembunyi : ", kata_tersembunyi)