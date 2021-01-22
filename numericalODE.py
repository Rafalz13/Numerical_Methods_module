import math
import matplotlib.pyplot as plt
import time


class RR:
    """ Klasa przeznaczona do obliczenia równania różniczkowego metodą Eulera i Rungego-Kutty.
        Parameters
        ----------
        func : funkcja przekazana
        t: czas początkowy
        t_stop : punkt końcowy czasu
        dt : krok czasowy
            domyślnie: dt = 0.1
        y: wartość znana

        Methods
        -------
        licz_euler
            metoda służąca do obliczenia metody Eulera zwraca tablice wyników
        licz_rk
            metoda służąca do obliczenia metody Rungego-Kutty zwraca tablice wyników """

    def __init__(self, func, y, t, t_stop, dt=0.1):
        self.func = func
        self.t_stop = t_stop
        self.dt = dt
        self.y = y
        self.n = int(t_stop / self.dt)
        self.t = t

    def licz_euler(self):
        """
        Returns
            -------
            wyniki
                lista z wartościami float
            T
                lista z punktami czasowe
        """
        self.y = 0.0
        x = 0.0
        T = []
        wyniki = []

        T.append(x)
        wyniki.append(self.y)

        for i in range(0, self.n, 1):
            self.y = self.y + self.dt * self.func(x, self.y)
            wyniki.append(self.y)
            x = x + self.dt
            T.append(x)

        return wyniki, T

    def licz_rk4(self):
        """
        Returns
        -------
        wyniki
            lista z wartościami float
        T
            lista z punktami czasowymi
        """
        self.y =  0.0
        x = 0.0
        T = []
        wyniki = []

        T.append(x)
        wyniki.append(self.y)

        for i in range(0, self.n, 1):
            k1 = self.dt * self.func(x, self.y)
            k2 = self.dt * self.func(x + self.dt * 0.5, 0.5 * k1 + self.y)
            k3 = self.dt * self.func(x + self.dt * 0.5, 0.5 * k2 + self.y)
            k4 = self.dt * self.func(x + self.dt, self.y + k3)

            self.y = self.y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            wyniki.append(self.y)

            x = x + self.dt
            T.append(x)

        return wyniki, T


class Blad:
    """ Klasa służąca do obliczenia różnicy miedzy wynikami uzystanych różnymi metodam.
        Przyjmuje 2 listy, które są porównywane. Wynikiem jest lista z wartościami różnic.
        Listy muszą mieć taki sam rozmiar.

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
            list_blad.append(math.fabs(wynik))

        return list_blad



