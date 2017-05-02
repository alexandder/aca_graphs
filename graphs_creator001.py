__author__ = 'aleksander'

import numpy as np
import matplotlib.pyplot as plt

elementary_neighborhoods = ['000', '001', '010', '011', '100', '101', '110', '111']


def compute_average_for_rule(rule, alphas):
    print("Avg for rule " + str(rule))
    result = {}
    for n in elementary_neighborhoods:
        result[n] = []
    for alpha in alphas:
        #print("Alpha: " + str(alpha) + ", rule " + str(170))
        fl = open('data001/' + str(rule) + '/' + str(alpha), 'r')
        abf_dict = eval(fl.read().strip().replace(" ", ""))
        fl.close()
        for nei in elementary_neighborhoods:
            result[nei].append(np.average(abf_dict[nei]))
    return result

def create_graph(averages, rule, alphas, path):
    plt.ylim([0,1.05])
    for n in ['000', '001', '010', '011', '101', '111']:
        plt.plot(alphas, averages[n], label = str(n))
    plt.xlabel(r'$\alpha$', size=20)
    plt.ylabel('averaged input-frequency', size=20)
    plt.title('Rule ' + str(rule))
    plt.legend(bbox_to_anchor=(0., 1.0, 1., .102), loc=3,
       ncol=4, mode="expand", borderaxespad=0.)
    plt.savefig(path)
    plt.close()


def create_graphs(rules, alphas):
    for r in rules:
        path = 'fig001/' + str(r) + '.pdf'
        avgs = compute_average_for_rule(r, alphas)
        create_graph(avgs, r, alphas, path)

alphas = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14,
          0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28,
          0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43,
          0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58,
          0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74,
          0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9,
          0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0]

rules88 = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 15,
           19, 22, 23, 24, 25, 26, 27, 29, 36, 43,
           44, 45, 46, 50, 54, 56, 57, 60, 62, 72, 77,
           78, 104, 105, 110, 126, 128, 132, 134, 136,
           140, 142, 170, 178, 184]

print (len(rules88))

create_graphs(rules88, alphas)
