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
        fl = open('data/' + str(rule) + '/' + str(alpha), 'r')
        abf_dict = eval(fl.read().strip().replace(" ", ""))
        fl.close()
        for nei in elementary_neighborhoods:
            result[nei].append(np.average(abf_dict[nei]))
    return result

def create_graph(averages, rule, alphas, path):
    plt.ylim([0,1.1])
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
        path = 'fig/' + str(r) + '.png'
        avgs = compute_average_for_rule(r, alphas)
        create_graph(avgs, r, alphas, path)

alphas = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

rules88 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 22, 23, 24, 25,
         26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 50, 51,
         54, 56, 57, 58, 60, 62, 72, 73, 74, 76, 77, 78, 90, 94, 104, 105, 106, 108, 110, 128,
         129, 130, 132, 134, 136, 138, 140, 142, 146, 150, 152, 154, 156, 160, 161, 162, 164, 168,
         170, 172, 178, 184, 200, 204, 232]

print (len(rules88))

create_graphs(rules88, alphas)