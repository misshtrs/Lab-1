import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#QUESTION 3i:

glist = []      #list of percents of connected graphs in each q
qlist = []      #list of q's
num = 0         #num of iterations in each q
connect = 0     #num of connected graphs in each q
for k in range(5, 105,5):
    q = k/100
    qlist.insert(num, q) 
    for i in range(0,10):
        G = nx.binomial_graph(20, q)
        #nx.draw(G, with_labels=True, font_weight='bold')
        #plt.show()
        if(nx.is_connected(G)==True):
           connect+=1
    connect = (connect/10)*100          #in percents
    glist.insert(num, connect)
    connect = 0
    num+=1
plt.plot(qlist,glist)
plt.show()
print(glist)
print(qlist)


#QUESTION 4i:

tlist = []      #list of percents of triangles in each n iteration
nlist = []      #list of n's
num = 0         #num of iterations in each n
triangles = 0     #num of triangles in each n iteration
for n in range(5, 205,5):
    nlist.insert(num, n) 
    for i in range(0,10):
        G = nx.binomial_graph(n, 0.5)
        triangles += sum(list(nx.triangles(G).values()))
    t3 = ((triangles/3)/10)         #in average
    tlist.insert(num, t3)
    t3 = 0
    triangles = 0
    num+=1
plt.plot(nlist,tlist)
plt.show()
print(tlist)
print(nlist)


#QUESTION 5i:

G1 = nx.path_graph(20)

f = 0
elist = []      #list of percents of connected graphs in each q
qlist = []      #list of q's
num = 0         #num of iterations in each q
removelist = []
for k in range(5, 105,5):
    q = k/100
    qlist.insert(num, q) 
    for d in range(0,10):
        iteredge = nx.non_edges(G1)   #touple of two nodes that checks if edge between them already exists
        for x in iteredge:
            if(q > (np.random.uniform())):
                G1.add_edge(*x)
                removelist.append(x)
        f += (sum(nx.eccentricity(G1).values())/20)
        G1.remove_edges_from(removelist)
    elist.insert(num, f/10)
    G1.remove_edges_from(removelist)
    removelist = []
    f = 0
    num+=1
plt.plot(qlist,elist)
plt.show()
print(elist)
print(qlist)


G2 = nx.cycle_graph(20)
p = 0
e2list = []      #list of percents of connected graphs in each q
qlist = []      #list of q's
num = 0         #num of iterations in each q
removelist = []

for k in range(5, 105,5):
    q = k/100
    qlist.insert(num, q) 
    for d in range(0,10):
        iteredge2 = nx.non_edges(G2)   #list of tuples of edges
        for x in iteredge2:
            if(q > (np.random.uniform())):
                G2.add_edge(*x)
                removelist.append(x)
        
        p += (sum(nx.eccentricity(G2).values())/20)
        G2.remove_edges_from(removelist)
    e2list.insert(num, p/10)
    G2.remove_edges_from(removelist)
    removelist = []
    p = 0
    num+=1
plt.plot(qlist,e2list)
plt.show()
print(e2list)
print(qlist)

