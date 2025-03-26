import math
import random

def realGradient(xy,f,m,max_iter,max_err,eta):
    l = len(f)
    a = [round(random.random(), 8) for i in range(m)]
    b = [round(random.random(), 8) for i in range(m)]
    c = [round(random.random(), 8) for i in range(m)]
    d = [round(random.random(), 8) for i in range(m)]
    p = [round(random.random(), 8) for i in range(m)]
    q = [round(random.random(), 8) for i in range(m)]
    r = [round(random.random(), 8) for i in range(m)]
    iter = 0
    while iter <= max_iter:
        alpha = []
        beta = []
        pi_arr = []
        err = 0.0
        o_arr = []
        sum_pi = []
        pi_z = []
        for i in range(l):
            alpha_current = []
            beta_current = []
            pi_current = []
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
                alpha_current.append(mi_a)
                beta_current.append(mi_b)
                pi_current.append(pi)
                z = p[j] * xy[i][0] + q[j] * xy[i][1] + r[j]
                brojnik += (z * pi)
                nazivnik += pi
            o = brojnik / nazivnik
            o_arr.append(o)
            sum_pi.append(nazivnik)
            pi_z.append(brojnik)
            pi_arr.append(pi_current)
            alpha.append(alpha_current)
            beta.append(beta_current)
            err += (0.5 * math.pow(f[i] - o, 2))
        if err <= max_err:
            print('Bravo')
            break
        else:
            print(str(iter) + ' ' + str(err))
            for i in range(m):
                a_add = 0.0
                b_add = 0.0
                c_add = 0.0
                d_add = 0.0
                p_add = 0.0
                q_add = 0.0
                r_add = 0.0
                for j in range(l):
                    a_add = round(
                        a_add + (f[j] - o_arr[j]) * ((xy[j][0] * sum_pi[j] - pi_z[j]) / math.pow(sum_pi[j], 2)) * \
                        beta[j][i] * b[i] * alpha[j][i] * (1 - alpha[j][i]), 8)
                    b_add = round(
                        b_add + (f[j] - o_arr[j]) * ((xy[j][0] * sum_pi[j] - pi_z[j]) / math.pow(sum_pi[j], 2)) * \
                        beta[j][i] * (xy[j][0] - a[i]) * alpha[j][i] * (1 - alpha[j][i]), 8)
                    c_add = round(
                        c_add + (f[j] - o_arr[j]) * ((xy[j][1] * sum_pi[j] - pi_z[j]) / math.pow(sum_pi[j], 2)) * \
                        alpha[j][i] * d[i] * beta[j][i] * (1 - beta[j][i]), 8)
                    d_add = round(
                        d_add + (f[j] - o_arr[j]) * ((xy[j][1] * sum_pi[j] - pi_z[j]) / math.pow(sum_pi[j], 2)) * \
                        alpha[j][i] * (xy[j][1] - c[i]) * beta[j][i] * (1 - beta[j][i]), 8)
                    p_add = round(p_add + (f[j] - o_arr[j]) * (pi_arr[j][i] / sum_pi[j]) * xy[j][0], 8)
                    q_add = round(q_add + (f[j] - o_arr[j]) * (pi_arr[j][i] / sum_pi[j]) * xy[j][1], 8)
                    r_add = round(r_add + (f[j] - o_arr[j]) * (pi_arr[j][i] / sum_pi[j]), 8)
                a[i] = a[i] - eta * a_add
                b[i] = b[i] - eta * b_add
                c[i] = c[i] - eta * c_add
                d[i] = d[i] - eta * d_add
                p[i] = p[i] - eta * p_add
                q[i] = q[i] + eta * q_add
                r[i] = r[i] - eta * r_add
            iter += 1

