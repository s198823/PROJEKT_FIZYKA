import numpy as np
import math
import matplotlib.pyplot as plt



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


t_w = None
h_max = None
t_k = None
z = None
                # rysowanie wykresu  dla rzutu ukosnego
if 0 < wynik_a < math.pi / 2:
            # Obliczenie zasięgu rzutu dla h_0 wieksze od 0
    if wynik_h0 > 0:
        if isinstance(wynik_h0, float) and isinstance(wynik_v, float) and isinstance(wynik_a, float) and isinstance(wynik_g, float):
            h_max = wynik_h0 + (((wynik_v ** 2) * (np.sin(wynik_a) ** 2)) / (2 * wynik_g))
        else:
            h_max = None
        if isinstance(wynik_g, float) and isinstance(wynik_v, float) and isinstance(wynik_a, float):
            z = ((wynik_v ** 2) * np.sin(wynik_a) * np.cos(wynik_a) / wynik_g) + (wynik_v * np.cos(wynik_a) * np.sqrt((2 * h_max) / wynik_g))
        else:
            z = None
    elif wynik_h0 == 0:
        if isinstance(wynik_g, float) and isinstance(wynik_v, float) and isinstance(wynik_a, float):
            z = (wynik_v ** 2 * np.sin(2 * wynik_a)) / wynik_g
        else:
            z = None
    else:
        z = None
                #czas wznoszenia dla rzutu ukośnego
    if isinstance(wynik_v, float) and isinstance(wynik_g, float) and isinstance(wynik_a, float):
        t_w = (wynik_v * np.sin(wynik_a)) / wynik_g
    if isinstance(wynik_v, float) and isinstance(wynik_g, float) and isinstance(wynik_a, float):
        t_k = ((wynik_v * np.sin(wynik_a))/wynik_g) + np.sqrt((2 * h_max)/wynik_g)




                #rysowanie wykresu dla rzutu poziomego
t_s = None
if wynik_a == 0:
    if wynik_h0 > 0:
        if isinstance(wynik_g, float) and isinstance(wynik_v, float) and isinstance(wynik_h0,float):
            z = wynik_v * np.sqrt((2 * wynik_h0) / wynik_g)
    else:
            z = None
                            #czas spadku
if isinstance(wynik_g, float) and isinstance(wynik_h0, float):
    t_s = np.sqrt((2*wynik_h0)/ wynik_g)


# Wyświetlanie wyników w konsoli
print("\n--- WYNIKI OBLICZEŃ ---")
print(f"Masa obiektu: {wynik_m} kg")
print(f"Przyspieszenie: {wynik_g} m/s^2")
print(f"Prędkość początkowa: {wynik_v} m/s")
print(f"Kąt alfa: {math.degrees(wynik_a):.2f}° ({wynik_a:.4f} rad)")
print(f"Wysokość początkowa: {wynik_h0} m")
print(f"Rodzaj rzutu: {rzut(wynik_a)}")
if t_s is not None:
    print(f"Czas spadku: {t_s} s")
if h_max is not None:
    print(f"Wysokosc maksymalna: {h_max} m")
else:
    print(f"Wysokość maksymalna równa sie wysokości początkowej: {wynik_h0} m")

if z is not None:
    print(f"Zasięg rzutu: {z:.2f} m")

if t_w is not None:
    print(f"Czas wznoszenia: {t_w} s")
if t_k is not None:
    print(f"Czas spadku: {t_k} s")


# Obliczenie toru lotu i wykres
if z is not None:
    if wynik_a == 0:
        x = np.linspace(0, z, 500)
        y = wynik_h0 - ((wynik_g * x**2)/2*wynik_v**2)

    if wynik_h0 == 0:
        x = np.linspace(0, z, 500)  # Więcej punktów dla płynności wykresu
        y = (x * np.tan(wynik_a)) - ((wynik_g * x ** 2) / (2 * (wynik_v ** 2) * (np.cos(wynik_a) ** 2)))
    elif wynik_h0 > 0:
        x = np.linspace(0, z,500)
        y = wynik_h0 + (x * np.tan(wynik_a)) - ((wynik_g * (x ** 2)) / (2 * (wynik_v ** 2) * (np.cos(wynik_a) ** 2)))

    # Filtrowanie wartości y >= 0 (żeby wykres nie wychodził poniżej ziemi)
    valid_indices = y >= 0
    x = x[valid_indices]
    y = y[valid_indices]

    # Rysowanie wykresu
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='g', label="Tor ruchu")
    plt.scatter(0, wynik_h0, color='red', label="Punkt Startowy")
    plt.scatter(z,0, color='blue', label="Punkt Końcowy")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Linia ziemi
    plt.title("Tor rzutu")
    plt.xlabel("Odległość (m)")
    plt.ylabel("Wysokość (m)")
    plt.legend()
    plt.grid()
    plt.show()
else:
    print("Nie udało się obliczyć toru lotu ze względu na nieprawidłowe dane wejściowe.")
                #rysowanie wykresu dla rzutu pionowego

if wynik_a == math.pi /2:
    if wynik_a == math.pi / 2:
        def wykres_pionowy(wynik_v, wynik_g, wynik_h0):
            # Obliczanie maksymalnej wysokości
            h_max2 = wynik_h0 + (wynik_v ** 2) / (2 * wynik_g)

            # Czas do osiągnięcia maksymalnej wysokości
            t_w2 = wynik_v / wynik_g

            # Całkowity czas ruchu (w górę i w dół)
            t_k2 = 2 * t_w2

            # Zakres czasu dla całego ruchu
            t = np.linspace(0, t_k2, 500)

            # Obliczanie wysokości w funkcji czasu
            h = wynik_h0 + wynik_v * t - 0.5 * wynik_g * t ** 2

            # Rysowanie wykresu
            plt.figure(figsize=(10, 6))
            plt.plot(np.zeros_like(t), h, label="Tor ruchu pionowego")
            plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Poziom gruntu
            plt.title("Tor rzutu pionowego")
            plt.xlabel("Czas (s)")
            plt.ylabel("Wysokość (m)")
            plt.legend()
            plt.grid()
            plt.show()


        wykres_pionowy(wynik_v, wynik_g, wynik_h0)

