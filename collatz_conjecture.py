### Sasha github.com/emoilenne ###

import matplotlib.pyplot as pyplot
from scipy.interpolate import spline
import numpy as np
import sys

# gather data
def generate_data():
    data = []
    print("Getting sequences of numbers...")
    for number in range(2, 101):
        print("Getting sequence for number %d..." % number)
        steps = [number]
        n = number
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
            steps.append(int(n))
        steps.reverse()
        data.append(np.array(steps))
    print("Generated data.")
    return data


# default representation
def mod0(data):
    pass

# mod 1 representation
def mod1(data):
    for graph in data:
        print(graph)
        number = graph[-1]
        new_x = np.linspace(graph.min(), graph.max(), 50) #TODO 50 change depending on size pf graph
        new_y = spline(graph, np.arange(0, len(graph)), new_x)
        pyplot.plot(new_x, new_y)

if __name__ == '__main__':
    pyplot.grid(False)
    pyplot.axis('off')

    data = generate_data()
    # mod1(data)
