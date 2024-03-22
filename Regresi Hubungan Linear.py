# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 20:14:43 2024

@author: Fadli Bilal
"""

import numpy as np
import matplotlib.pyplot as plt

# ngebaca data dari file teks
nama_file = input("Masukkan nama file teks: ")
data = np.genfromtxt(nama_file, skip_header=1)

# misahin kolom kecepatan aliran dan koefisien kekasaran saluran
x = data[:, 1]  # kolom kecepatan Aliran
y = data[:, 0]  # kolom koefisien kekasaran Saluran

# perintah buat regresi linear menggunakan metode least squares
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

# buatin Plot data dan garis regresi
plt.plot(x, y, 'o', label='Data')
plt.plot(x, m*x + c, 'r', label='Regresi Linear')
plt.xlabel('Kecepatan Aliran (m/s)')
plt.ylabel('Koefisien Kekasaran Saluran')
plt.title('Regresi Linear')
plt.legend()

# nampilin persamaan regresi
plt.text(0.5, 0.9, f'Persamaan: y = {m:.3f}x + {c:.3f}', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

plt.show()