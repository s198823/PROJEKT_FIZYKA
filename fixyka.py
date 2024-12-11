import math
import numpy as np
# pętle while żeby od razu wyświetlało błedy po wpisaniu nieodpowiedniej wartośic, ograniczenie dla wysokosci do 100 m
def masa():
    try:
        m = float(input("Podaj masę punktu [kg]: "))
        if m <= 0:  # warunek
            return "Masa musi być większa od 0"
        return m #zwraca mase
    except ValueError:
        return "Podana wartość nie jest liczbą" #np. dla wpisania litery zamiast cyfry

def przyspieszenie():
    try:
        g = float(input("Podaj przyspieszenie [m/s^2]: "))
        if g < 0:  # warunek
            return "Przyspieszenie nie może być ujemne"
        return g #zwraca przyspieszenie ziemskie
    except ValueError:
        return "Podana wartość nie jest liczbą"

def predkosc():
    try:
        v_0 = float(input("Podaj wartość prędkości początkowej [m/s]: "))
        v_1 = 7900
        if v_0 > v_1 :  # warunek
            return "Prędkość początkowa nie może być większa od pierwszej wartości kosmicznej (7900 m/s)"
        elif v_0 < 0:
            return "Predkosc poczatkowa nie moze byc ujemna"
        return v_0 #zwraca predkosc poczatkowa
    except ValueError:
        return "Podana wartość nie jest liczbą"

def alfa():
    try:
        a = float(input("Podaj kat pomiedzy predkoscia a ziemia: "))
        if a > 90:
            return "Kąt nie moze wynosic wiecej niz 90 stopni"
        elif a < 0:
            return "Kąt nie moze byc ujemny"
        kat_radiany = np.radians(a) #zamiana a na radiany
        return kat_radiany #wypisanie a jako radiany
    except ValueError:
        return "Podana wartosc nie jest liczba"

def wysokosc():
    try:
        h_0 = float(input("Podaj wysokosc poczatkowa: "))
        if h_0 < 0:
            return "Wysokosc poczatkowa nie moze byc ujemna"
        return h_0
    except ValueError :
        return "Podana wartosc nie jest liczba"

def rzut(a):
    if a == 0:
        return "RZUT POZIOMY"
    elif 0 < a < math.pi / 2: #zakres miedzy 0 a po stopni
        return "RZUT UKOŚNY"
    elif a == math.pi /2 : #rowne 90 stopni
        return "RZUT PIONOWY"

# Wywołanie funkcji
wynik_m = masa()
wynik_g = przyspieszenie()
wynik_v = predkosc()
wynik_a = alfa()
wynik_h0 = wysokosc()
wynik_rzut = rzut(wynik_a)


print(f"Masa: {wynik_m}")
print(f"Przyspieszenie: {wynik_g}")
print(f"Prędkość początkowa: {wynik_v}")
print(f"Kąt alfa: {wynik_a}")
print(f"Wysokosc poczatkowa: {wynik_h0}")
print(f"Rodzaj rzutu: {rzut(wynik_a)}")