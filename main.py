import math
import matplotlib.pyplot as plt
import time
from abc import ABC, abstractmethod
from scipy import integrate
import numpy as np

from numericalODE import RK4, Euler, CalcError
from functions import fun_exp, lot_volt_f, lot_volt_g, to_1dim, exact


#warunki początkowe
t = 0.0
t_stop = 80.0

dt = 0.1
dt_e = 0.1

y = 1.0
y0 = [30,4]
func = fun_exp

params = {
    'a': 0.2,   # współczynnik nardzin ofiar
    'b': 0.04,   # czestotliwosc umierania ofiar
    'c': 0.04,   # przyrost drapieżników
    'd': 0.5    # umieranie drapieżnikow
    }
# tuple - do Scipy
params_ =[v for _, v in params.items()]
params_= tuple(params_)

# obliczenia
euler_1 = Euler(fun_exp, y, t, t_stop, dt)
rk4_1 = RK4(fun_exp, y, t, t_stop, dt)

# Lotki-Volterry, ukad równań różniczkowych
Ye_2dim, Te_2dim = euler_1.solve_system(f=lot_volt_f, g=lot_volt_g, u=y0, params=params)
Yrk_2dim, Trk_2dim = rk4_1.solve_system(f=lot_volt_f, g=lot_volt_g, u=y0, params=params)
preyRK, predRK = to_1dim(Yrk_2dim)
preyE, predE = to_1dim(Ye_2dim)

# wizualizacja
plt.figure(figsize=(15,8))
plt.plot(Te_2dim, Ye_2dim, label="E")
plt.plot(Trk_2dim, Yrk_2dim, label="RK")
plt.xlabel("czas")
plt.ylabel("liczba zwierząt")
plt.legend()
plt.show()

# równanie różniczkowe
t_stop = 40
euler_2 = Euler(fun_exp, y, t, t_stop, dt)
rk4_2 = RK4(fun_exp, y, t, t_stop, dt)

Ye, Te = euler_2.solve()
Yrk, Trk = rk4_2.solve()
exact_rk = exact(dt,t_stop,y)

#wizualizacja
plt.figure(figsize=(16,10))
plt.plot(Te,Ye, color="red", label=f"Euler dt: {dt_e}")
plt.plot(Trk,exact_rk, label="exact")
plt.xlabel("czas",fontsize=13)
plt.ylabel("y",fontsize=13)
plt.legend()
plt.show()