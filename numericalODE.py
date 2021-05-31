import math
import matplotlib.pyplot as plt
import time
from abc import ABC, abstractmethod

class RR(ABC):
    """ Klasa przeznaczona do obliczenia równania różniczkowego metodą Eulera i Rungego-Kutty."""


    def __init__(self, func, y, t, t_stop, dt=0.1):
        """
        Parameters
        ----------
        func: function
            przekazana funkcja
        y: float
            wartość znana, y początkowe
        t: float
            czas początkowy
        t_stop: float
            punkt końcowy czasu
        dt: float
            krok czasowy
        """
        self.func = func
        self.t_stop = t_stop
        self.dt = dt
        self.y = y
        self.n = int(t_stop / self.dt)
        self.t0 = t

    @abstractmethod
    def solve(self): pass

    @abstractmethod
    def solve_time(self, dt, t_stop): pass

    @abstractmethod
    def solve_system(self, f, g, u, params): pass


class Euler(RR):
    """
    Klasa służy do rozwiązywania równań różniczkowych metodami numerycznymi

    Methods:
    --------
    solve
        służy do rozwiązywania równań różniczkowych
    solve_time
        służy do mierzenia czasu obliczeń
    licz_uklad_rownań
        służy do rozwiązywania  układu równań różniczkowych

    """
    def __init__(self, func, y, t, t_stop, dt):
        """
        Parameters
        ----------
        func: function
            przekazana funkcja
        y: float
            wartość znana, y początkowe
        t: float
            czas początkowy
        t_stop: float
            punkt końcowy czasu
        dt: float
            krok czasowy
        """
        super().__init__(func, y, t, t_stop, dt)

    def solve(self):
        """
        Metoda służąca do rozwiązywania równania metoda Eulera.
        Zwraca tablicę z wynikami oraz tablicę z punktami czasowymi.

        Returns:
        -------
             wyniki - lista z wartościami float,

             T - lista z punktami czasowymi
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

    def solve_time(self,dt, t_stop):
        """
        Metoda służy do obliczenia wartości na danym punkcie t_stop, obliczenia bez operacji na listach.

        Parameters
        ----------
        dt: float
            krok czasowy
        t_stop: float
            punkt czasowy na którym zwracna jest wartość

        Returns
        ---------
        ret
            y - wartość wyniku na podanym punkcie t_stop,

            czas -  czas jaki trwaly obliczenia
        """
        start2 = time.time()
        y = self.y

        # przypisanie na początku żeby y nie brało z innej funkcji tylko to oryginalne początkowe
        x = self.t0
        n = int(t_stop / dt)  # ilośc punktów/powtórzen

        for i in range(0, n, 1):
            y = y + dt * self.func(x, y)
            x = x + dt

        end2 = time.time()
        czas = end2 - start2
        # print(f'[Euler] czas bez list: {czas}')
        return y, czas

    def solve_system(self, f, g, u, params):
        """
        Parameters
        ----------
        f: function
            funkcja f
        g: function
            funkcja g
        u: list
            wektor przechowujący 2 wartości początkowe
        params: dict
            parametry do funkcji w formie słownika

        Returns
        ---------
        ret
            wyniki - wyniki w postaci listy przechowującej wektory,

            T- lista kroków czasowych
        """
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


class RK4(RR):
    """
    Klasa służy do rozwiązywania równań różniczkowych metodami numerycznymi

    Methods:
    --------
    solve
        służy do rozwiązywania równań różniczkowych
    solve_time
        służy do mierzenia czasu obliczeń
    licz_uklad_rownań
        służy do rozwiązywania  układu równań różniczkowych

    """
    def __init__(self, func, y, t, t_stop, dt):
        """
        Parameters
        ----------
        func: function
            przekazana funkcja
        y: float
            wartość znana, y początkowe
        t: float
            czas początkowy
        t_stop: float
            punkt końcowy czasu
        dt: float
            krok czasowy
        """
        super().__init__(func, y, t, t_stop, dt)

    def solve(self):
        """
        Metoda służąca do rozwiązywania równania metodą Rungego-Kutty czwartego rzędu.
        Zwraca tablicę z wynikami oraz tablicę z punktami czasowymi.

        Returns
        -------
        ret
             wyniki - lista z wartościami float,

             T - lista z punktami czasowymi
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

    def solve_time(self, dt, t_stop):
        """
        Metoda służy do obliczenia wartości na danym punkcie t_stop, obliczenia bez operacji na listach.

        Parameters
        ----------
        dt: float
            krok czasowy
        t_stop: float
            punkt czasowy na którym zwracna jest wartość

        Returns
        ---------
        ret
            y - wartość wyniku na podanym punkcie t_stop,

            czas -  czas jaki trwaly obliczenia

        """

        start2rk = time.time()

        y = self.y
        x = self.t0
        n = int(t_stop / dt)

        for i in range(0, n, 1):
            k1 = dt * self.func(x, y)
            k2 = dt * self.func(x + dt * 0.5, 0.5 * k1 + y)
            k3 = dt * self.func(x + dt * 0.5, 0.5 * k2 + y)
            k4 = dt * self.func(x + dt, y + k3)

            y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            x = x + dt

        end2rk = time.time()
        czas = end2rk - start2rk
        # print(f'[RK4] czas bez list: {czas}')
        return y, czas

    def solve_system(self, f, g, u, params):
        """
        Parameters
        ----------
        f: function
            funcja f
        g: function
            funkcja g
        u: list
            wektor [x,y] przechowujący 2 wartości początkowe
        params: dict
            parametry do funkcji w formie słownika

        Returns
        ---------
        ret
            wyniki - wyniki w postaci listy przechowującej wektory,

            T- lista kroków czasowych
        """
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


class CalcError:

    """
    Klasa służąca do obliczenia różnicy miedzy wynikami uzystanych różnymi metodam.
    Przyjmuje 2 listy, które są porównywane. Wynikiem jest lista z wartościami różnic.
    Listy muszą mieć taki sam rozmiar.

    Functions
    ----------
    absolute
        metoda wyliczająca błąd bezwzględny
    relative
        metoda wyliczająca błąd względny
    """

    def __init__(self, lista1, lista2):
        """
        Parameters
        ----------
        lista1: list
            wartości dokładne typu float
        lista2: list
            wartości mierzone typu float
        """
        self.lista1 = lista1
        self.lista2 = lista2

    def absolute(self):
        """
        Metoda służy do liczenia błędu bezwzględnego

        Return:
        ---------
        lista_blad: list
            lista z wartościami float"""

        list_blad = []
        for x, y in zip(self.lista1, self.lista2):
            wynik = x - y
            list_blad.append(math.fabs(wynik))

        return list_blad

    def relative(self):
        """
        Metoda służy do liczenia błędu bezwzględnego

        Return:
        ----------
        lista_blad: list
            lista z wartościami float"""

        list_blad = []
        for x, y in zip(self.lista1, self.lista2):
            dx = y - x
            wynik = (dx / x)  # *100 ->jesli bedzie blad procentowy
            list_blad.append(math.fabs(wynik))

        return list_blad



