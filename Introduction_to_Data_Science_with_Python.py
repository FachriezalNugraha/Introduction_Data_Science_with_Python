#!/usr/bin/env python
# coding: utf-8
Python adalah bahasa pemrograman yang ditujukan untuk general-purpose programming dan termasuk dalam kategori high-level programming language.

Sebagai general-purpose programming language, Python digunakan untuk berbagai macam permasalahan seperti: pengembangan aplikasi web ataupun mobile, data science, dll.

Python masuk ke dalam kategori high-level programming language dikarenakan bahasa pemrograman Python yang mudah untuk dibaca dan dituliskan oleh manusia.

Bahasa  pemrograman  Python  diciptakan  oleh  Guido  van Rossum dan pertama kali diperkenalkan pada tahun 1991 sebagai sebuah proyek open-source. Lisensi dari Python bersifat open-source dari Python atau dengan kata lain setiap orang dapat mengembangkan program komputer dengan menggunakan bahasa pemrograman Python baik untuk tujuan komersil/non-komersil.

Python adalah bahasa yang ditujukan untuk general-purpose programming, jenis high-level programming language dan berlisensi open sourceLibrary dalam python

Numpy (numerical python) adalah library yang memudahkan dalam pendefinisian array baik 1D, 2D, 3D atau nD, dan juga memiliki fungsi-fungsi untuk aljabar linier.

Scipy (Scientific Python) merupakan library yang ditujukan untuk keperluan komputasi saintifik seperti keperluan aljabar linier, integrasi dan diferensiasi numerik, transformasi Fourier, optimasi, interpolasi, statistik dan yang lainnya.

Pandas adalah library untuk pengolahan data dalam bentuk tabular (seperti excel) yang merupakan de facto library bagi data scientist dalam mengolah data dari berbagai sumber seperti file CSV, TSV, Excel, SQL queries, Google BigQuery, SAS, Stata, SPSS, dsb.

Matplotlib digunakan untuk visualisasi dari data ke dalam berbagai bentuk grafik 2D atau 3D, seperti line chart, bar chart, histogram, polar chart, error bar plot, dan jenis grafik lainnya.

Scikit-learn adalah Scipy Toolkit yang ditujukan untuk menghasilkan model predictive dengan menggunakan machine learning.
Seaborn merupakan library yang dibuat dari matplotlib yang ditujukan oleh visualisasi grafik statistik dengan warna yang menawan, terintegrasi dengan baik dengan pandas.Struktur Bahasa Python - Part 2
Aku menyimak tampilan layar laptop, berusaha memahami catatan Senja untuk struktur bahasa Python yang dapat aku gunakan:

No.

Struktur

Keterangan

1

Statements

instruksi yang diberikan secara baris per baris untuk dijalankan oleh program

2

Variables

pengindentifikasian yang  digunakan untuk menampung sebuah data atau informasi

3

Literals

data atau informasi yang digunakan untuk mengisi suatu variabel

4

Operators

simbol-simbol yang digunakan untuk mengubah nilai dari satu variabel dengan melibatkan satu atau lebih variabel dan literal.

5

Reserved Words

kumpulan kata-kata yang memiliki makna khusus dalam bahasa pemrograman Python dan tidak dapat digunakan untuk variables dan literals

6

Whitespace

pada bahasa Python, spasi dan tab memiliki makna khusus untuk menandai serangkaian blok dalam kode Python

7

Comments

merupakan sekumpulan teks yang dituliskan di dalam sebuah program yang tidak akan mempengaruhi hasil dari sebuah programPython “Hello World” & Statement
# In[1]:


print("Hello World.")
print("Saya Aksara, baru belajar Python.")

Variables di Python
Sekarang kita akan membahas teknik penulisan variables pada Python dengan mengikuti contoh ini yang sudah disediakan Senja
# In[2]:


bil1 = 10
Bil_2 = 20
Frasa = "Halo Dunia"
bil1, Bil_2 = 10, 20
salam = "Selamat Pagi"; Penutup = "Salam Sejahtera"

Comments di Python
Comments adalah sekumpulan teks yang dituliskan di dalam sebuah program yang tidak akan mempengaruhi hasil dari sebuah program.
# In[3]:


# perintah pada baris ini tidak mempengaruhi program
'''
perintah ini tidak akan dieksekusi oleh Python
dan perintah ini juga tidak akan dieksekusi
perintah ini juga tidak akan dieksekusi
'''
print("jadi # digunakan untuk membuat comment pada Python")


# In[ ]:




