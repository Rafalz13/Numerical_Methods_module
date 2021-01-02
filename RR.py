from math import *

class RR:

    def __init__(self, fun, zakres, krok=0.1):
        self.fun = fun
        self.zakres = zakres
        self.krok = krok

    def licz_euler(self):
        licz, wynik = 0, 1
        x = 0.0
        wyniki = []

        # obliczenie przyblizenia
        while x <= self.zakres:
            funkcja = eval(self.fun)
            wynik = wynik - 0.05 * wynik * funkcja
            x += self.krok
            x = round(x, 1)
            licz += 1
            wyniki.append(wynik)

        return wyniki

    def licz_rk(self):
        licz, wynik = 0, 1
        x = 0.0
        wyniki = []

        # obliczenie przyblienia
        while x <= self.zakres:
            fun_m1 = eval(self.fun)
            x += self.krok
            fun_x = eval(self.fun)
            wynik = wynik - 0.05 * wynik * fun_m1 - 0.05 * fun_x * (1 - 0.1 * fun_m1) * wynik
            x = round(x, 1)
            licz += 1
            wyniki.append(wynik)

        return wyniki



class Blad:
    def __init__(self, list1, list2):
        self.lista1 = list1
        self.lista2 = list2

    def licz(self):
        list_blad = []
        for x, y in zip(self.lista1, self.lista2):
            wynik = x - y
            list_blad.append(fabs(wynik))

        return list_blad


