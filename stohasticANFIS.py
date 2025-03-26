import math
import random
import sys

def stohastic(xy,f,m,max_iter,max_err,eta):
    l = len(f)
    a = [round(random.random(), 8) for i in range(m)]
    b = [round(random.random(), 8) for i in range(m)]
    c = [round(random.random(), 8) for i in range(m)]
    d = [round(random.random(), 8) for i in range(m)]
    p = [round(random.random(), 8) for i in range(m)]
    q = [round(random.random(), 8) for i in range(m)]
    r = [round(random.random(), 8) for i in range(m)]

    iter = 0
    current = 0
    while iter <= max_iter:
        err = 0.0
        o_current = -1
        sum_pi = 0.0
        pi_arr = []
        pi_z = 0.0
        alpha = []
        beta = []
        for i in range(l):
            brojnik = 0.0
            nazivnik = 0.0
            for j in range(m):
                try:
                    mi_a = 1 / (1 + math.exp(b[j] * (xy[i][0] - a[j])))
                except OverflowError:
                    mi_a = 0.00000001
                try:
                    mi_b = 1 / (1 + math.exp(d[j] * (xy[i][1] - c[j])))
                except OverflowError:
                    mi_b = 0.00000001
                pi = mi_a * mi_b
                if i == current:
                    alpha.append(mi_a)
                    beta.append(mi_b)
                    pi_arr.append(pi)
                z = p[j] * xy[i][0] + q[j] * xy[i][1] + r[j]
                brojnik += (z * pi)
                nazivnik += pi
            o = brojnik / nazivnik
            if i == current:
                o_current = o
                sum_pi = nazivnik
                pi_z = brojnik
            err += (0.5 * math.pow(f[i] - o, 2))
        if err <= max_err:
            print('Success')
            return a,b,c,d,p,q,r
        else:
            print(str(iter) + ' ' + str(err))
            for i in range(m):
                a_old = a[i]
                c_old = c[i]
                a[i] = round(
                    a[i] - eta * (f[current] - o_current) * ((xy[current][0] * sum_pi - pi_z) / math.pow(sum_pi, 2)) * \
                    beta[i] * b[i] * alpha[i] * (1 - alpha[i]), 8)
                b[i] = round(
                    b[i] - eta * (f[current] - o_current) * ((xy[current][0] * sum_pi - pi_z) / math.pow(sum_pi, 2)) * \
                    beta[i] * (xy[current][0] - a_old) * alpha[i] * (1 - alpha[i]), 8)
                c[i] = round(
                    c[i] - eta * (f[current] - o_current) * ((xy[current][1] * sum_pi - pi_z) / math.pow(sum_pi, 2)) * \
                    alpha[i] * d[i] * beta[i] * (1 - beta[i]), 8)
                d[i] = round(
                    d[i] - eta * (f[current] - o_current) * ((xy[current][1] * sum_pi - pi_z) / math.pow(sum_pi, 2)) * \
                    alpha[i] * (xy[current][1] - c_old) * beta[i] * (1 - beta[i]), 8)
                p[i] = round(p[i] - eta * (f[current] - o_current) * (pi_arr[i] / sum_pi) * xy[current][0], 8)
                q[i] = round(q[i] - eta * (f[current] - o_current) * (pi_arr[i] / sum_pi) * xy[current][1], 8)
                r[i] = round(r[i] - eta * (f[current] - o_current) * (pi_arr[i] / sum_pi), 8)
            iter += 1
            current += 1
            if current >= l:
                current = 0
