import os
import string

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from sys import argv
from networkx.drawing.nx_agraph import write_dot

def laplacian(path):
    laplacian = np.array([
        [0,1,0,0,1,0],
        [1,0,1,0,1,0],
        [0,1,0,1,0,0],
        [0,0,1,0,1,1],
        [1,1,0,1,0,0],
        [0,0,0,1,0,0]
    ])

    num_nodes = laplacian.shape[0]
    ascii_labels = list(string.ascii_uppercase[:num_nodes])
    numeric_labels = list(range(num_nodes))
    mapping = dict(zip(numeric_labels, ascii_labels))

    G = nx.from_numpy_array(laplacian)
    G = nx.relabel_nodes(G, mapping)

    write_dot(G, '{0}/dot/laplacian.dot'.format(path))
    os.system('neato -Tpng {0}/dot/laplacian.dot -o {0}/png/laplacian.png'.format(path))

def main():
    laplacian(argv[1])

if __name__ == '__main__':
    main()
