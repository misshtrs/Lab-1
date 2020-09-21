import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms import approximation

glist = []      #list of percents of connected graphs in each n
nlist = []      #list of n's
num = 0         #num of iterations in each n
connect = 0     #num of connected graphs in each n
steinerlist = []
mstlist = []
scount = 0
mcount = 0

for n in range(8, 48,8):
    p = 5/n
    nlist.insert(num, n) 
    for i in range(0,20):
        G = nx.path_graph(n)
        iteredge = nx.non_edges(G)   #touple of two nodes that checks if edge between them already exists
        for x in iteredge:
            if(p > (np.random.uniform())):
                G.add_edge(*x, weight=np.random.randint(1, 6))
        if(nx.is_connected(G)==True):
            a = list(G.nodes)
            scount += nx.algorithms.approximation.steinertree.steiner_tree(G, a[:int(n/2)]).size()/20
            mcount += nx.minimum_spanning_tree(G).size()/20   
    glist.insert(num, scount/mcount)
    scount = mcount = 0
    num+=1
    
plt.plot(nlist,glist)
plt.show()
print(glist)
print(nlist)
