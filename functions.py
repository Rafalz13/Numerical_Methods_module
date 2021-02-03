import math


def fun_exp(x,y):
    y = math.exp(-0.2*x) * math.sin(2*x ) + (math.cos(0.2*x))*0.1
    return y


def exact(dt, t_stop, y, x=0.0):
    Y_exact = []
    for i in range(int(t_stop / dt) + 1):
        y = 0.5 * math.sin(0.2 * x) - 0.049505 * math.exp(-0.2 * x) * math.sin(2 * x) - 0.49505 * math.exp(
            -0.2 * x) * math.cos(2 * x) + 1.49505
        Y_exact.append(y)
        x = x + dt

    # exact_exp(modyfikacja) 0.5*math.sin(0.2*x)-0.049505 *math.exp(-0.2*x)*math.sin(2*x)-0.49505*math.exp(-0.2*x)*math.cos(2*x) + 1.49505
    # exact sin:    1-math.cos(x)
    # exact x:      math.pow(x,3)/3
    # exact exp:    -0.049505*math.exp(-0.2*x)*math.sin(2*x) - 0.49505*math.exp(-0.2*x)*cos(2*x) + 0.49505
    return Y_exact


def lot_volt_f(t, x, y, params):
    a = params['a']
    b = params['b']

    dxdt = a * x - b * x * y
    return dxdt


def lot_volt_g(t, x, y, params):
    c = params['c']
    d = params['d']

    dydt = c * x * y - d * y
    return dydt


def to_1dim(Y):
    y1 = [row[0] for row in Y]
    y2 = [row[1] for row in Y]

    return y1, y2


def wyniki_blad(blad_type, dt, i_check=None):
    blad = blad_type
    rozmiar = len(blad)
    err_min = 100.0
    i_check = i_check / dt

    for i in range(rozmiar):
        if blad[i] < err_min:
            err_min = blad[i]
            min_step = i

        if i == i_check:
            print(f'wynik na punkcie {int(i_check)}: {blad[i]}')

    print(f'min: {err_min}, step: {min_step}/{rozmiar}')
