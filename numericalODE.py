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
        self.t0 = t

    def licz_euler(self):
        """
        Returns
            -------
            wyniki
                lista z wartościami float
            T
                lista z punktami czasowe
        """
        y = self.y
        x = self.t0
        T = []
        wyniki = []

        T.append(x)
        wyniki.append(y)

        for i in range(0, self.n, 1):
            y = y + self.dt * self.func(x, y)
            wyniki.append(y)
            x = x + self.dt
            T.append(x)

        return wyniki, T

    def licz_euler_light(self):
        """
        Returns
        -------
        y
            ostatni wynik
        """
        y = self.y
        x = self.t0
        n = int(self.t_stop / self.dt)

        for i in range(0, n, 1):
            y = y + self.dt * self.func(x, y)
            x = x + self.dt

        return y

    def licz_euler_2dim(self, f, g, u, params):
        x = u[0]
        y = u[1]

        T = []
        wyniki = []
        n = int(self.t_stop / self.dt)
        t = self.t0
        T.append(t)
        wyniki.append([x, y])

        for i in range(0, n, 1):
            x = x + self.dt * f(t, x, y, params)
            y = y + self.dt * g(t, x, y, params)

            wyniki.append([x, y])
            t = t + self.dt
            T.append(t)

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

        y = self.y
        x = self.t0
        T = []
        wyniki = []

        T.append(x)
        wyniki.append(self.y)

        for i in range(0, self.n, 1):
            k1 = self.dt * self.func(x, y)
            k2 = self.dt * self.func(x + self.dt * 0.5, 0.5 * k1 + y)
            k3 = self.dt * self.func(x + self.dt * 0.5, 0.5 * k2 + y)
            k4 = self.dt * self.func(x + self.dt, y + k3)

            y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            wyniki.append(y)

            x = x + self.dt
            T.append(x)

        return wyniki, T


    def licz_rk4_light(self):
        """
        Returns
        -------
        y
            ostatni wynik
        """
        y = self.y
        x = self.t0
        n = int(self.t_stop / self.dt)

        for i in range(0, n, 1):
            k1 = self.dt * self.func(x, y)
            k2 = self.dt * self.func(x + self.dt * 0.5, 0.5 * k1 + y)
            k3 = self.dt * self.func(x + self.dt * 0.5, 0.5 * k2 + y)
            k4 = self.dt * self.func(x + self.dt, y + k3)

            y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            x = x + self.dt

        return y

    def licz_rk4_2dim(self, f, g, u, params):
        x = u[0]
        y = u[1]
        t = self.t0
        n = int(self.t_stop / self.dt)
        T = []
        wyniki = []

        wyniki.append([x, y])
        T.append(t)

        for i in range(0, n, 1):
            k1 = f(t, x, y, params)
            l1 = g(t, x, y, params)
            k2 = f(t + self.dt / 2, x + self.dt * k1 / 2, y + self.dt * l1 / 2, params)
            l2 = g(t + self.dt / 2, x + self.dt * k1 / 2, y + self.dt * l1 / 2, params)
            k3 = f(t + self.dt / 2, x + self.dt * k2 / 2, y + self.dt * l2 / 2, params)
            l3 = g(t + self.dt / 2, x + self.dt * k2 / 2, y + self.dt * l2 / 2, params)
            k4 = f(t + self.dt, x + self.dt * k3, y + self.dt * l3, params)
            l4 = g(t + self.dt, x + self.dt * k3, y + self.dt * l3, params)

            k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
            l = (l1 + 2 * l2 + 2 * l3 + l4) / 6
            x = x + self.dt * k
            y = y + self.dt * l
            t = t + self.dt

            T.append(t)
            wyniki.append([x, y])

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


def fun_exp(x,y):
    y = math.exp(-0.2*x) * math.sin(2*x)
    return y
