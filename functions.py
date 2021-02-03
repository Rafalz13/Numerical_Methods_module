import math


def fun_exp(x, y):
    y = math.exp(-0.2*x) * math.sin(2*x)
    return y


def exact(dt, t_stop,y, x=0.0 ):
    Y_exact = []
    for i in range(int(t_stop / dt) + 1):
        y = -0.049505*math.exp(-0.2*x)*math.sin(2*x) - 0.49505*math.exp(-0.2*x)*math.cos(2*x) + 0.49505
        Y_exact.append(y)
        x = x + dt
    # exact sin:    1-math.cos(x)
    # exact x:      math.pow(x,3)/3
    # exact exp:    -0.049505*math.exp(-0.2*x)*math.sin(2*x) - 0.49505*math.exp(-0.2*x)*cos(2*x) + 0.49505
    return Y_exact
