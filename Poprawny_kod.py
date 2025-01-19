import numpy as np
import math
import matplotlib.pyplot as plt

# Funkcje do obsługi wejścia

def masa():
    while True:
        try:
            m = float(input("Podaj masę punktu [kg]: "))
            if m <= 0:
                print("Masa musi być większa od 0.")
                continue
            return m
        except ValueError:
            print("Podana wartość nie jest liczbą. Spróbuj ponownie.")

def przyspieszenie():
    while True:
        try:
            g = float(input("Podaj przyspieszenie [m/s^2]: "))
            if g <= 0:
                print("Przyspieszenie musi być większe od 0.")
                continue
            return g
        except ValueError:
            print("Podana wartość nie jest liczbą. Spróbuj ponownie.")

def predkosc():
    while True:
        try:
            v_0 = float(input("Podaj wartość prędkości początkowej [m/s]: "))
            v_1 = 7900  # Pierwsza prędkość kosmiczna
            if v_0 > v_1:
                print("Prędkość początkowa nie może być większa od 7900 m/s.")
                continue
            elif v_0 < 0:
                print("Prędkość początkowa nie może być ujemna.")
                continue
            return v_0
        except ValueError:
            print("Podana wartość nie jest liczbą. Spróbuj ponownie.")

def alfa():
    while True:
        try:
            a = float(input("Podaj kąt pomiędzy prędkością a ziemią [stopnie]: "))
            if a > 90:
                print("Kąt nie może być większy niż 90 stopni.")
                continue
            elif a < 0:
                print("Kąt nie może być ujemny.")
                continue
            return np.radians(a)  # Zamiana na radiany
        except ValueError:
            print("Podana wartość nie jest liczbą. Spróbuj ponownie.")

def wysokosc():
    while True:
        try:
            h_0 = float(input("Podaj wysokość początkową [m]: "))
            if h_0 < 0:
                print("Wysokość początkowa nie może być ujemna.")
                continue
            elif h_0 > 100:
                print("Wysokość początkowa nie może być większa niż 100 m.")
                continue
            return h_0
        except ValueError:
            print("Podana wartość nie jest liczbą. Spróbuj ponownie.")

# Funkcje obliczeniowe

def oblicz_ukosny(wynik_h0, wynik_v, wynik_a, wynik_g):
    h_max = wynik_h0 + ((wynik_v**2) * (np.sin(wynik_a)**2)) / (2 * wynik_g)
    z = ((wynik_v**2) * np.sin(wynik_a) * np.cos(wynik_a) / wynik_g) + (wynik_v * np.cos(wynik_a) * np.sqrt((2 * h_max) / wynik_g))
    t_w = (wynik_v * np.sin(wynik_a)) / wynik_g
    t_k = ((wynik_v * np.sin(wynik_a))/wynik_g) + np.sqrt((2 * h_max)/wynik_g)
    return h_max, z, t_w, t_k

def oblicz_pionowy(wynik_h0, wynik_v, wynik_g):
    h_max = wynik_h0 + (wynik_v**2) / (2 * wynik_g)
    t_w = wynik_v / wynik_g
    t_k = t_w + np.sqrt(2 *h_max / wynik_g)
    return h_max, t_w, t_k

def oblicz_poziomy(wynik_h0, wynik_v, wynik_g):
    if wynik_h0 > 0:
        z = wynik_v * np.sqrt((2 * wynik_h0) / wynik_g)
        t_s = np.sqrt((2 * wynik_h0) / wynik_g)
    return z, t_s


# Funkcje rysujące wykresy

def rysuj_ukosny(x, y, wynik_h0, z):
    valid_indices = y >= 0
    x = x[valid_indices]
    y = y[valid_indices]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='g', label="Tor ruchu")
    plt.scatter(0, wynik_h0, color='red', label="Punkt Startowy")
    plt.scatter(z, 0, color='blue', label="Punkt Końcowy")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.title("Tor rzutu ukośnego")
    plt.xlabel("Odległość (m)")
    plt.ylabel("Wysokość (m)")
    plt.legend()
    plt.grid()
    plt.show()

def rysuj_poziomy(x, y, wynik_h0, z):

    valid_indices = y >= 0
    x = x[valid_indices]
    y = y[valid_indices]

    # Rysowanie wykresu
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='g', label="Tor ruchu")
    plt.scatter(0, wynik_h0, color='red', label="Punkt Startowy")
    plt.scatter(z,0, color='blue', label="Punkt Końcowy")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Linia ziemi
    plt.title("Tor rzutu poziomego")
    plt.xlabel("Odległość (m)")
    plt.ylabel("Wysokość (m)")
    plt.legend()
    plt.grid()
    plt.show()

def rysuj_pionowy(t, h, wynik_h0):
    # Zakres czasu dla całego ruchu

    t = np.linspace(0, t_k, 500)

    # Obliczanie wysokości w funkcji czasu
    h = wynik_h0 + wynik_v * t - 0.5 * wynik_g * t ** 2

    # Filtracja danych, aby obiekt nie opadał poniżej ziemi
    valid_indices = h >= 0
    x = np.zeros_like(t[valid_indices])
    h = h[valid_indices]

    plt.figure(figsize=(6, 10))  # Odwrócenie proporcji dla lepszego efektu
    plt.plot(x, h, label="Tor ruchu pionowego", color="g")
    plt.scatter(0, wynik_h0, color='red', label="Punkt startowy")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Poziom ziemi
    plt.title("Tor rzutu pionowego")
    plt.xlabel("Odległość (m)")
    plt.ylabel("Wysokość (m)")
    plt.legend()
    plt.grid()
    plt.show()

# Główna logika programu

wynik_m = masa()
wynik_g = przyspieszenie()
wynik_v = predkosc()
wynik_a = alfa()
wynik_h0 = wysokosc()

if 0 < wynik_a < math.pi / 2:
    h_max, z, t_w, t_k = oblicz_ukosny(wynik_h0, wynik_v, wynik_a, wynik_g)
    x = np.linspace(0, z, 500)
    y = wynik_h0 + (x * np.tan(wynik_a)) - ((wynik_g * (x**2)) / (2 * (wynik_v**2) * (np.cos(wynik_a)**2)))
    rysuj_ukosny(x, y, wynik_h0, z)

elif wynik_a == math.pi / 2:
    h_max, t_w, t_k = oblicz_pionowy(wynik_h0, wynik_v, wynik_g)
    t = np.linspace(0, t_k, 500)
    h = wynik_h0 + wynik_v * t - 0.5 * wynik_g * t**2
    rysuj_pionowy(t, h, wynik_h0)

elif wynik_a == 0:
    z, t_s = oblicz_poziomy(wynik_h0, wynik_v, wynik_g)
    x = np.linspace(0, z, 500)
    y = wynik_h0 - ((wynik_g * x**2)/(2*wynik_v**2))
    rysuj_poziomy(x, y, wynik_h0, z)



# Wyświetlanie wyników
print("\n--- WYNIKI OBLICZEŃ ---")
print(f"Masa obiektu: {wynik_m} kg")
print(f"Przyspieszenie: {wynik_g} m/s^2")
print(f"Prędkość początkowa: {wynik_v} m/s")
print(f"Kąt alfa: {math.degrees(wynik_a):.2f}° ({wynik_a:.4f} rad)")
print(f"Wysokość początkowa: {wynik_h0} m")
if 0 < wynik_a < math.pi / 2:
    print(f"Wysokość maksymalna: {h_max:.2f} m")
    print(f"Zasięg rzutu: {z:.2f} m")
    print(f"Czas wznoszenia: {t_w:.2f} s")
    print(f"Całkowity czas ruchu: {t_k:.2f} s")
elif wynik_a == math.pi / 2:
    print(f"Wysokość maksymalna: {h_max:.2f} m")
    print(f"Czas do maksymalnej wysokości: {t_w:.2f} s")
    print(f"Całkowity czas ruchu: {t_k:.2f} s")
elif wynik_a == 0:
    print(f"Zasięg rzutu: {z:.2f} m")
    print(f"Czas spadku: {t_s:.2f} s")
