from math import *

# 2 -  =C2-0,05*C2*SIN(A2)-0,05*SIN(A3)*(1-0,1*SIN(A2))*C2 - poniżej błąd, nie mam wartości dla sin(a3) czyli dla x ni poprzedniego tylko x równego krokiem funkcji

# =C3-0,05*C3*SIN(A3) a3 - krok+krok, e3-poprzednia funkcja
#         sin(X),0.1,3


class RR:
    """ Klasa przeznaczona do obliczenia równania różniczkowego metodą Eulera i Rungego-Kutty.
        Parametry
        ---------- 
        fun : string ( sin(x)**2 )
        zakres : float 
        krok : wartośc domyślna to 0.1

        Metody
        -------
        licz_euler
            metoda służąca do obliczenia metody Eulera zwraca tablice wyników
        licz_rk
            metoda służąca do obliczenia metody Rungego-Kutty zwraca tablice wyników """

    def __init__(self, fun, zakres, krok=0.1):
        self.fun = fun
        self.zakres = zakres
        self.krok = krok

    def licz_euler(self):
        """
        Returns
        -------
        wyniki
            lista z wartościami float"""

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
        """
        Returns
        -------
        wyniki
            lista z wartościami float"""

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
    """ Klasa służąca do obliczenia błędu obliczeń miedzy określonymi metodami
        Przyjmuje 2 listy, które są porównywane i przekazane na wykres.

        Parametry
        ----------
        lista1, lista2
            listy z wartościami float

        Metody
        ----------
        licz
            metoda wyliczająca różnicę między wartościami w listach """

    def __init__(self, list1, list2):
        self.lista1 = list1
        self.lista2 = list2

    def licz(self):
        """
        Returns:
        ----------
        lista_blad
            lista z wartościami float"""

        list_blad = []
        for x, y in zip(self.lista1, self.lista2):
            wynik = x - y
            list_blad.append(fabs(wynik))

        return list_blad


