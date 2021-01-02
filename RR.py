from math import *

class Euler:
    ''' Klasa przeznaczona do obliczenia równania różniczkowego metodą Eulera '''

    def __init__(self, fun,zakres, krok=0.1):
        self.fun = fun
        self.zakres = zakres
        self.krok = krok

    def __iter__(self):
        pass

    def licz(self):
        ''' metoda służąca do obliczenia metody Eulera zwraca tablice wyników '''

        licz, wynik = 0, 1
        x = 0.0
        wyniki = []

        ''' obliczenie przyblizenia 
        '''
        while x <= self.zakres:
            fun_ev = eval(self.fun)
            wynik = wynik - 0.05 * wynik * fun_ev
            x += self.krok
            x = round(x, 1)
            licz += 1
            wyniki.append(wynik)
        return wyniki


class RunKutta:
    ''' Klasa przeznaczona do obliczenia równania różniczkowego metodą Rungego-Kutty '''

    def __init__(self,fun, zakres, krok=0.1):
        self.fun = fun
        self.zakres = zakres
        self.krok = krok

    def licz(self):
        ''' metoda służąca do obliczenia metody Eulera zwraca tablice wyników '''
        licz, wynik = 0, 1
        x = 0.0
        wyniki = []
        ''' obliczenie przyblienia '''
        while x <= self.zakres:
            fun_m1 = eval(self.fun)
            print(f'x: {x}')
            x += self.krok
            fun_x = eval(self.fun)
            print(f'new x: {x}')
            wynik = wynik - 0.05 * wynik * fun_m1 - 0.05 * fun_x * (1 - 0.1 * fun_m1) * wynik
            x = round(x, 1)
            licz += 1
            wyniki.append(wynik)

        return wyniki


class MetodaAnalityczna:
    def __init__(self,fun, zakres, krok=0.1):
        self.fun = fun
        self.zakres = zakres
        self.krok = krok

    def licz(self):
        licz, wynik = 0, 1
        x = 0.0
        wyniki = []
        ''' obliczenie przybliżenia '''
        while x <= self.zakres:
            print("przed eval")
            funkc = eval(self.fun)
            print("po eval")

            x += self.krok
            wynik = funkc
            x = round(x, 1)
            licz += 1
            wyniki.append(wynik)

        return wyniki


class Blad:
    ''' metoda służąca do obliczenia błędu miedzy określonymi metodami '''

    def __init__(self,list1, list2):
        self.lista1 = list1
        self.lista2 = list2

    def licz(self):
        list_blad = []
        for x, y in zip(self.lista1, self.lista2):
            wynik = x - y
            list_blad.append(fabs(wynik))
        return list_blad
