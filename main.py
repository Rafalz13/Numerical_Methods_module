from numericalODE import RR, Blad
import math
import matplotlib.pyplot as plt

# Funkcje
def fun_sin(x,y):
    y = math.sin(x)
    return y

def fun_x(x,y):
    y = x**2
    return y

def fun_exp(x,y):
    y = math.exp(-0.2*x) * math.sin(2*x )
    return y

def exact(dt, t_stop,y, x=0.0 ):
    Y_exact = []
    for i in range(int(t_stop / dt) + 1):
        y = math.pow(x,3)/3
        Y_exact.append(y)
        x = x + dt
    # exact sin:    1-math.cos(x)
    # exact x:      math.pow(x,3)/3
    # exact exp:    0.049505*math.exp(0.2*x)*math.sin(2*x) - 0.49505*math.exp(0.2*x)*cos(2*x) + 0.49505
    return Y_exact

# Warunki początkowe
t = 0.0
t_stop = 20.0
dt =0.01
y = 0.0
func = fun_x

#Analitycznie
Y_exact = exact(dt = dt, t_stop = t_stop, y = y)

#obiekty
rownanie1 = RR(func, t=t, y=y, t_stop=t_stop, dt=dt)
Y_e, T = rownanie1.licz_euler()
Y_rk, T = rownanie1.licz_rk4()

#Błąd
blad1 = Blad(Y_rk,Y_e)
blad1_list = blad1.licz()

# ------------------------------------

#wizualizacja
plt.figure(figsize=(16,5), dpi= 90)
plt.title(f'Dla funkcji : {func.__name__}')
plt.xlabel("time")
plt.ylabel("y")

plt.plot(T,Y_e, color="green",label='Euler')
plt.plot(T,Y_rk, color="red",label='Runge-Kutta')
# plt.plot(T,Y_exact, color="blue",label='Exact')

plt.legend(loc='upper right', fontsize='x-large')
plt.grid(True)

plt.show()
#
# plt.plot(T, blad1_list)
# plt.show()
