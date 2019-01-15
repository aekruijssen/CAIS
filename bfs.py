# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:45:11 2017

@author: adina
"""

from gurobipy import *
import numpy as np

#import gurobipy
#from gorubipy import Model, Var, Constr
m=Model()

"""
Add decision variables to model
 Xi = {1 if node selected, 0 otherwise}
 
 {X1=0, X2=0, ... Xn=0}
"""
x = m.addVar(lb=0, ub=1, vtype=GRB.BINARY)
x1 = m.addVar (lb=0, ub=1, obj=0.0, vtype=GRB.BINARY)
x2 = m.addVar (lb=0, ub=1, obj=0.0, vtype=GRB.BINARY)
x3 = m.addVar (lb=0, ub=1, obj=0.0, vtype=GRB.BINARY)
x4 = m.addVar (lb=0, ub=1, obj=0.0, vtype=GRB.BINARY)
x5 = m.addVar (lb=0, ub=1, obj=0.0, vtype=GRB.BINARY)
x6 = m.addVar (lb=0, ub=1, obj=0.0, vtype=GRB.BINARY)
x7 = m.addVar (lb=0, ub=1, obj=0.0, vtype=GRB.BINARY)

Dictionary = [x1, x2, x3, x4, x5, x6, x7] #nodes Xi from 1 to 7

graph = [x1[x2,x4], x2[x1,x3], x3[x2,x5], x4[x1,x5,x6,x7], 
        x5[x3,x4,x7], x6[x4,x7], x7[x4,x5]] #nodes and their connections

adj = [x1[0,0,0,0,0,0,0], x2[0,0,0,0,0,0,0], x3[0,0,0,0,0,0,0], 
       x4[0,0,0,0,0,0,0], x5[0,0,0,0,0,0,0], x6[0,0,0,0,0,0,0], x7[0,0,0,0,0,0,0]]
for node in adj:
    for connection in graph[node]:
        if connection == x1: adj[node[0]] = 1
        if connection == x2: adj[node[1]] = 1
        if connection == x3: adj[node[2]] = 1
        if connection == x4: adj[node[3]] = 1
        if connection == x5: adj[node[4]] = 1
        if connection == x6: adj[node[5]] = 1
        if connection == x7: adj[node[6]] = 1

"""
Above code established connections of all nodes through each node's
connections array, where seven values correspond to each node in graph
    Ex: x1 will be [0,1,0,1,0,0,0], where x1 shares edges with x2 & x4
Now, the nodes themselves must be labelled 
"""

m.update()

"""
Set objective function -> Summation of Xi
minimum number of edges to cover all nodes in graph
"""
m.setObjective(np.sum(x),GRB.MINIMIZE())

"""
Add constraints -> 
 for each node j, delta(j)={all nodes that share edge with j}
 for node i there exists a node that is selected such that it is in delta(i)
 Vj: Summation of Xi sub delta(j) >= 1
"""
m.addConstr()

m.optimize()