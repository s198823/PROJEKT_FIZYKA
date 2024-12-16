import numpy as np
import math
import matplotlib.pyplot as plt
from pandas.core.indexers import validate_indices


# Pętla while dla poprawności wejścia użytkownika
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


def rzut(a):
    if a == 0:
        return "RZUT POZIOMY"
    elif 0 < a < math.pi / 2:
        return "RZUT UKOŚNY"
    elif a == math.pi / 2:
        return "RZUT PIONOWY"


# Pobranie wartości od użytkownika
wynik_m = masa()
wynik_g = przyspieszenie()
wynik_v = predkosc()
wynik_a = alfa()
wynik_h0 = wysokosc()

# Obliczenie zasięgu rzutu
if isinstance(wynik_g, float) and isinstance(wynik_v, float) and isinstance(wynik_a, float):
    z = (wynik_v ** 2 * np.sin(2 * wynik_a)) / wynik_g
else:
    z = None

# Wyświetlanie wyników w konsoli
print("\n--- WYNIKI OBLICZEŃ ---")
print(f"Masa obiektu: {wynik_m} kg")
print(f"Przyspieszenie ziemskie: {wynik_g} m/s^2")
print(f"Prędkość początkowa: {wynik_v} m/s")
print(f"Kąt alfa: {math.degrees(wynik_a):.2f}° ({wynik_a:.4f} rad)")
print(f"Wysokość początkowa: {wynik_h0} m")
print(f"Rodzaj rzutu: {rzut(wynik_a)}")

if z is not None:
    print(f"Zasięg rzutu: {z:.2f} m")

# Obliczenie toru lotu i wykres
if z is not None:
    x = np.linspace(0, z, 500)  # Więcej punktów dla płynności wykresu
    y = (x * np.tan(wynik_a)) - ((wynik_g * x ** 2) / (2 * (wynik_v ** 2) * (np.cos(wynik_a) ** 2)))

    # Dodanie wysokości początkowej
    y += wynik_h0

    # Filtrowanie wartości y >= 0 (żeby wykres nie wychodził poniżej ziemi)
    valid_indices = y >= 0
    x = x[valid_indices]
    y = y[valid_indices]

    # Rysowanie wykresu
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='g', label="Tor ruchu")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Linia ziemi
    plt.title("Tor rzutu")
    plt.xlabel("Odległość (m)")
    plt.ylabel("Wysokość (m)")
    plt.legend()
    plt.grid()
    plt.show()
else:
    print("Nie udało się obliczyć toru lotu ze względu na nieprawidłowe dane wejściowe.")
