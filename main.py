from numericalODE import RR, Blad
from functions import *
import matplotlib.pyplot as plt

# Warunki początkowe
t = 0.0
t_stop = 20.0
dt =0.1
y = 0.0
func = fun_exp

#Analitycznie
Y_exact = exact(dt=dt, t_stop=t_stop, y=y)

#obiekty
rownanie1 = RR(func, t=t, y=y, t_stop=t_stop, dt=dt)
Y_e, T = rownanie1.licz_euler()
Y_rk, T = rownanie1.licz_rk4()

#Błąd
blad1 = Blad(Y_rk, Y_exact)
blad1_list = blad1.licz()

# ------------------------------------

#wizualizacja
plt.figure(figsize=(16,5), dpi= 90)
plt.title(f'Dla funkcji : {func.__name__}')
plt.xlabel("time")
plt.ylabel("y")

plt.plot(T,Y_e, color="green",label='Euler')
plt.plot(T,Y_rk, color="red",label='Runge-Kutta')
plt.plot(T,Y_exact, color="blue",label='Exact')

plt.legend(loc='upper right', fontsize='x-large')
plt.grid(True)
plt.show()

plt.plot(T, blad1_list)
plt.show()
