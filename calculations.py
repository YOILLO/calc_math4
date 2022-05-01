import random


def lagranz_method(x, y, t):
    ans = 0
    for i in range(len(y)):
        l = y[i]
        for j in range(len(x)):
            if i != j:
                l *= (t - x[j]) / (x[i] - x[j])
        ans += l
    return ans


def get_points_from_func(f, a, b, step, sigma):
    x = []
    y = []
    x_now = a
    while x_now <= b:
        x.append(random.gauss(x_now, sigma))
        y.append(random.gauss(f(x_now), sigma))
        x_now += step
    return x, y
