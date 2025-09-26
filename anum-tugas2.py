# TUGAS:
### 1. Buat fungsi sinusoidal:
   f(x) = sin(x) + (1/2)sin(2x) + (1/3)sin(3x) + (1/4)sin(4x) + (1/5)sin(5x)
   dengan interval x = [0, 10], jumlah titik 500.

### 2. Hitung turunan f'(x) dan integral kumulatif F(x) untuk interval tersebut.
   (50% nilai)

### 3. Hitung integral secara terpisah:
   - Bagian integral di atas sumbu y=0
   - Bagian integral di bawah sumbu y=0
   (25% nilai)

### 4. Buat plot semua fungsi:
   - f(x), f'(x), dan F(x)
   - Plot F(x) disertai area di atas dan di bawah y=0 dengan warna berbeda
   (25% nilai)

   # Nama: Olivia Natasya Yuniar
# NPM: 24083010012

import numpy as np
import matplotlib.pyplot as plt

# Interval
x = np.linspace(0, 10, 500)
dx = x[1] - x[0]

# Definisi fungsi f(x)
f = np.sin(x) + 0.5*np.sin(2*x) + (1/3)*np.sin(3*x) + (1/4)*np.sin(4*x) + (1/5)*np.sin(5*x)

# Turunan analitik f'(x) = cos(x) + cos(2x) + cos(3x) + cos(4x) + cos(5x)
f_prime = np.cos(x) + np.cos(2*x) + np.cos(3*x) + np.cos(4*x) + np.cos(5*x)

# Plot f(x) dan f'(x)
plt.figure(figsize=(8,4))
plt.plot(x, f, label="f(x)")
plt.plot(x, f_prime, label="f'(x)", linestyle="--")
plt.axhline(0, color="black", linewidth=0.8)
plt.title("Fungsi f(x) dan Turunannya f'(x)")
plt.legend()
plt.grid(True)
plt.show()


# Integral analitik F(x) = -cos(x) - 1/4 cos(2x) - 1/9 cos(3x) - 1/16 cos(4x) - 1/25 cos(5x) + C
F_analytic = -(np.cos(x) + (1/4)*np.cos(2*x) + (1/9)*np.cos(3*x) + (1/16)*np.cos(4*x) + (1/25)*np.cos(5*x))
F_analytic = F_analytic - F_analytic[0]  # set konstanta supaya F(0)=0

# Integral kumulatif numerik (trapezoid rule)
F_numeric = np.zeros_like(f)
for i in range(1, len(x)):
    F_numeric[i] = F_numeric[i-1] + 0.5*(f[i-1] + f[i]) * dx

# Plot hasil integral
plt.figure(figsize=(8,4))
plt.plot(x, F_numeric, label="F(x) numerik")
plt.plot(x, F_analytic, label="F(x) analitik", linestyle="--")
plt.title("Integral Kumulatif F(x)")
plt.legend()
plt.grid(True)
plt.show()


# Bagian positif dan negatif dari f(x)
f_pos = np.where(f > 0, f, 0)
f_neg = np.where(f < 0, f, 0)

# Integral area positif dan negatif
I_pos = np.trapz(f_pos, x)
I_neg = np.trapz(f_neg, x)
I_total = np.trapz(f, x)

print("Integral total  =", I_total)
print("Integral positif =", I_pos)
print("Integral negatif =", I_neg)

# Plot area positif (biru) dan negatif (merah)
plt.figure(figsize=(8,4))
plt.plot(x, f, label="f(x)")
plt.axhline(0, color="black", linewidth=0.8)
plt.fill_between(x, f, 0, where=f>0, color="skyblue", alpha=0.5, label="Area f>0")
plt.fill_between(x, f, 0, where=f<0, color="salmon", alpha=0.5, label="Area f<0")
plt.title("f(x) dengan Area Positif dan Negatif")
plt.legend()
plt.grid(True)
plt.show()


# Integral kumulatif positif dan negatif
F_pos = np.zeros_like(f)
F_neg = np.zeros_like(f)
for i in range(1, len(x)):
    F_pos[i] = F_pos[i-1] + 0.5*(f_pos[i-1] + f_pos[i]) * dx
    F_neg[i] = F_neg[i-1] + 0.5*(f_neg[i-1] + f_neg[i]) * dx

# Plot kumulatif
plt.figure(figsize=(8,4))
plt.plot(x, F_numeric, label="F total (numeric)")
plt.plot(x, F_pos, linestyle="--", label="F positif")
plt.plot(x, F_neg, linestyle="--", label="F negatif")
plt.title("Kontribusi Integral Kumulatif")
plt.legend()
plt.grid(True)
plt.show()
