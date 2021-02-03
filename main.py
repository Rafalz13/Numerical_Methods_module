from numericalODE import RR, Blad
from functions import *
import matplotlib.pyplot as plt

# Warunki początkowe
t = 0.0
t_stop = 50.0
dt = 0.1
dt_e = 0.05
y = 1.0
y0 = [20,2]
func = fun_exp
params = {
    'a': 0.6,   # współczynnik nardzin ofiar
    'b': 0.2,   # czestotliwosc umierania ofiar
    'c': 0.1,   # przyrost drapieżników
    'd': 0.4    # umieranie drapieżnikow
    }

#Analitycznie
Y_exact_e = exact(dt_e, t_stop, y)
Y_exact_rk = exact(dt, t_stop, y)

#obiekty
rownanie1 = RR(func, t=t, y=y, t_stop=t_stop, dt=dt)
rownanie2 = RR(func, t=t, y=y, t_stop=t_stop, dt=dt_e)
#Euler
Y_e, Te = rownanie2.licz_euler()
Y_el = rownanie2.licz_euler_light()
#Runge Kutta
Y_rk, Trk = rownanie1.licz_rk4()
Y_rkl = rownanie1.licz_rk4_light()

#Błąd
blad1 = Blad(Y_exact_rk,Y_rk)
blad_bezwzgl_rk = blad1.licz_bezwzg()
blad_wzgl_rk = blad1.licz_wzg()


wyniki_blad(blad_wzgl_rk[1:],dt, 20) # jezeli dla Eulera-> zmienić nazwe błędu i dt dla Eulera
# ------------------------------------

plt.figure(figsize=(16,5),dpi= 80)
# plt.plot(Trk, blad_bezwzgl,color="red", label="bezwzgledny")
plt.plot(Trk, blad_wzgl_rk, color="green", label="wzgledny-RK4")
plt.xlabel("time",fontsize=15)
plt.ylabel("blad",fontsize=15)
plt.legend()
plt.show()

#wizualizacja
plt.figure(figsize=(16,5), dpi= 90)
plt.title(f'Dla funkcji : {func.__name__}')
plt.xlabel("time")
plt.ylabel("y")

plt.plot(Te,Y_e, color="orange",label='Euler')
plt.plot(Trk,Y_rk, color="red",label='Runge-Kutta')
plt.plot(Te,Y_exact_e, color="blue",label='Exact_euler')
plt.plot(Trk,Y_exact_rk, color="purple",label='Exact_RK')

plt.legend(loc='upper right', fontsize='x-large')
plt.grid(True)

plt.show()

