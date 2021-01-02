from RR_class import *
from math import *
import matplotlib.pyplot as plt

#zmienne
zakres = 25
krok =0.1
funkcja = 'sin(3.0-x**2)'

#iksy na wykresie
h = 0.0
list_h = []
while h <= zakres+0.1:
    list_h.append(h)
    h += krok


#Euler
D1 = RR(funkcja,zakres,krok)
wynikE = D1.licz_euler()

#Runge Kutta
wynikRK = D1.licz_rk()

#Błąd
blad = Blad(wynikRK,wynikE)
wynik_blad = blad.licz()

#wizualizacja
plt.figure(figsize=(14,8), dpi= 80)
plt.title(f'Dla funkcji : {funkcja}')
#plt.xlabel("time")
#plt.ylabel("y")
plt.plot(list_h,wynikE, color="green",label='Euler')
plt.plot(list_h,wynikRK, color="red",label='Runge-Kutta')
plt.plot(list_h,wynik_blad, color="blue",label='Blad')
plt.legend(loc='upper right', shadow=1, fontsize='x-large')
plt.grid(True)
plt.show()

# blad1 = Blad(wynikRK,wynikE)
# blad1_list = blad1.licz()
# plt.figure(figsize=(14,8),dpi= 80)
# plt.plot(list_h,wynik_blad)
# plt.show()