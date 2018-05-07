#!/bin/env python3

# Propogates uncertainty
# Copy-paste the output into your favorite
# text editor and format the output from there

# Run 'sudo -H pip install tabulate' first

from tabulate import tabulate


class MinMax(object):
    def __init__(self, min, max):
        self.min, self.max = min, max


def get_minmaxes(uncert, values):
    try:
        iter(uncert)
    except:
        uncert = [uncert for i in range(len(values))]
    mins = [values[i] - uncert[i] for i in range(len(values))]
    maxes = [values[i] + uncert[i] for i in range(len(values))]
    return list(zip(values, mins, maxes))


def get_minmax(uncert, value):
    return (value, value - uncert, value + uncert)


def calc_values(n, func, **kwargs):
    minmaxes = [{k: v[i] for k, v in kwargs.items()} for i in range(n)]
    mid_results = [func(**{k: MinMax(v[0], v[0]) for k, v in e.items()}) for e in minmaxes]
    min_results = [func(**{k: MinMax(v[1], v[2]) for k, v in e.items()}) for e in minmaxes]
    max_results = [func(**{k: MinMax(v[2], v[1]) for k, v in e.items()}) for e in minmaxes]
    return list(zip(mid_results, max_results, min_results))


def print_values(n, title, minmaxes):
    uncerts = [max(abs(v[0] - v[1]), abs(v[0] - v[2])) for v in minmaxes]
    table = [[str(e) for e in minmaxes[i]] + [str(uncerts[i])] for i in range(n)]
    print(f'\n{title}\n')
    print(tabulate(table, headers=["Value", "Min", "Max", "Uncertainty (max dev.)"]))
    print('\n\n')


values_do = get_minmaxes(0.05, [30, 35.12, 39.99, 45, 49.98, 55.01, 59.83, 65.1])
values_di = get_minmaxes(0.3, [55.5, 43.5, 39.1, 35.8, 33.3, 31.5, 30.3, 29])

n = len(values_do)

values_ho = [get_minmax(0.01, 3.20)] * n
values_hi = get_minmaxes(0.1, [-5.9, -3.9, -3, -2.4, -2, -1.7, -1.6, -1.3])

f_max = lambda do, di: 1 / (1 / do.max + 1 / di.max)
md_max = lambda do, di: - di.min / do.max
mh_max = lambda ho, hi: hi.max / ho.min


print_values(n, 'FOCAL LENGTH', calc_values(n, f_max, do=values_do, di=values_di))
print_values(n, 'MAGNIFICATION (DISTANCE)', calc_values(n, md_max, do=values_do, di=values_di))
print_values(n, 'MAGNIFICATION (HEIGHT)', calc_values(n, mh_max, ho=values_ho, hi=values_hi))
