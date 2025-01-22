import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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


# Funkcje rysujące wykresy wraz z animacjami

def rysuj_ukosny(x, y, wynik_h0, z):

    # Filtracja danych (y >= 0)
    valid_indices = y >= 0
    x = np.array(x)[valid_indices]
    y = np.array(y)[valid_indices]

    # Rysowanie wykresu
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, color='g', label="Tor ruchu")
    ax.scatter(0, wynik_h0, color='yellow', label="Punkt Startowy")
    ax.scatter(z, 0, color='blue', label="Punkt Końcowy")
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Poziom ziemi
    ax.set_title("Tor rzutu ukośnego")
    ax.set_xlabel("Odległość (m)")
    ax.set_ylabel("Wysokość (m)")
    ax.legend()
    ax.grid()

    # Punkt animowany
    point, = ax.plot([], [], 'ro', label="Ruch punktu materialnego")

    # Funkcja inicjalizująca animację
    def init():
        point.set_data([], [])
        return point,

    # Funkcja aktualizująca pozycję punktu w animacji
    def update(frame):
        point.set_data([x[frame]], [y[frame]])  # listy jednoelementowe, aby otrzymać współrzędne punktu
        return point,

    # Tworzenie animacji
    ani = FuncAnimation(fig, update, frames=len(x), init_func=init, interval=15, blit=True, repeat=True)
    # frames=len(x) - liczba klatek (liczba punktów na torze), interval=20 - czas trwania każdej klatki w ms, repeat=True - ciągłe odtwarzanie animacji

    # Wyświetlenie wykresu z animacją
    plt.show()

def rysuj_poziomy(x, y, wynik_h0, z):

    valid_indices = y >= 0
    x = x[valid_indices]
    y = y[valid_indices]

    # Rysowanie wykresu
    fig,ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, color='g', label="Tor ruchu")
    ax.scatter(0, wynik_h0, color='yellow', label="Punkt Startowy")
    ax.scatter(z, 0, color='blue', label="Punkt Końcowy")
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--') #Poziom ziemi
    ax.set_title("Tor rzutu poziomego")
    ax.set_xlabel("Odległość (m)")
    ax.set_ylabel("Wysokość (m)")
    ax.legend()
    ax.grid()

    # Punkt animowany
    point, = ax.plot([], [], 'ro', label="Ruch punktu materialnego")

    # Funkcja inicjalizująca animację
    def init():
        point.set_data([], [])
        return point,

    # Funkcja aktualizująca pozycję punktu w animacji
    def update(frame):
        point.set_data([x[frame]], [y[frame]])  # listy jednoelementowe, aby otrzymać współrzędne punktu
        return point,

    # Tworzenie animacji
    ani = FuncAnimation(fig, update, frames=len(x), init_func=init, interval=15, blit=True, repeat=True)
    # frames=len(x) - liczba klatek (liczba punktów na torze), interval=20 - czas trwania każdej klatki w ms, repeat=True - ciągłe odtwarzanie animacji

    # Wyświetlenie wykresu z animacją
    plt.show()



def rysuj_pionowy(wynik_h0, wynik_v, wynik_g):
    # Czas do osiągnięcia maksymalnej wysokości
    t_w = wynik_v / wynik_g

    # Maksymalny czas (ruch do ziemi)
    t_k = (wynik_v + np.sqrt(wynik_v ** 2 + 2 * wynik_g * wynik_h0)) / wynik_g #taki sam jak przy obliczaniu, ale z podstawieniem za t_w

    # Pełny zakres czasu od początku ruchu w górę do dotkniecia ziemi przez punkt materialny
    t = np.linspace(0, t_k, 500)

    # Obliczanie wysokości w funkcji czasu
    h = wynik_h0 + wynik_v * t - 0.5 * wynik_g * t ** 2 #wzór na drogę z położeniem i prędkością początkową w ruchu opóźnionym

    # Rysowanie wykresu
    fig, ax = plt.subplots(figsize=(6, 10))
    ax.set_xlim(-1, 1)  # Stała szerokość osi X (ruch pionowy)
    ax.set_ylim(0, np.max(h) + 5)  # Oś Y do maksymalnej wysokości + 5m dla czytelności
    ax.set_xlabel("Odległość (m)")
    ax.set_ylabel("Wysokość (m)")
    ax.set_title("Tor rzutu pionowego")
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--') #Poziom ziemi
    ax.plot(np.zeros_like(h), h, label="Tor ruchu pionowego", color="g", alpha=0.5) #stała wartość x=0
    ax.scatter(0, wynik_h0, color='yellow', label="Punkt Startowy", zorder=5)

    # Punkt reprezentujący ciało w ruchu
    point, = ax.plot([], [], 'ro', label="Ruch punkt materialnego", markersize=8)

    # Funkcja inicjalizująca animację
    def init():
        point.set_data([0], [wynik_h0])  # Ustawienie początkowego punktu jako h0
        return point,

    # Funkcja aktualizująca pozycję punktu w animacji
    def update(frame):
        # Obliczanie aktualnego indeksu w ramach pełnego ruchu (góra-dół i powtórzenie)
        current_index = frame % len(h)
        current_h = h[current_index]  # Aktualna wysokość
        point.set_data([0], [current_h])  # Współrzędne punktu
        return point,

    # Tworzenie animacji, aktualizowanie punktu co 15 ms
    ani = FuncAnimation(fig, update, frames=len(h) * 2, init_func=init, blit=True, interval=15)
    # frames=len(h) - liczba klatek (liczba punktów na torze), interval=20 - czas trwania każdej klatki w ms, repeat=True - ciągłe odtwarzanie animacji

    # Wyświetlenie wykresu z animacją
    ax.legend()
    plt.show()


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
    rysuj_pionowy(wynik_h0, wynik_v, wynik_g)

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