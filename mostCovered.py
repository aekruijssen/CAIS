# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:49:25 2018

@author: adina
"""

from gurobipy import *
adj = {} # dict in python
filehandle=open("sim_graph_barabasi.txt", "r")

for line in filehandle.readlines():
    current_line = line.split(":")
    node = int(current_line[0])
    to_split = current_line[1]
    ngh = [int(x) for x in to_split.split(",")] #array of a node's neighbors
    adj[node]=ngh # adj list: array of each node's neighbors array
    
#print(adj)
#print('num of elements', len(adj.keys()))

def get_all_elements(adj):
    all_elements = []
    for e in adj:
        if e not in all_elements:
            all_elements.append(e)
        neighbours = adj[e]
        for e1 in neighbours:
            if e1 not in all_elements:
                all_elements.append(e1)
                #print(e1)
    return all_elements #array of each node (ex: [1, 2, 3, ...])

#print(get_all_elements(adj))

def mostCovered(adj):
    key_list = [x for x in adj.keys()]
    #print(key_list)
    all_ele = get_all_elements(adj)
    m = gurobipy.Model()
    x = [] #decision variable x, Xi = 1 if node at pos i is chosen, 0 if not
    y = [] #decision variable y, Yi = 1 if node at pos i is covered, 0 if not
    for i in range(0, len(all_ele)):
        x.append(m.addVar(vtype=gurobipy.GRB.BINARY, name='x_'+str(i)))
        y.append(m.addVar(vtype=gurobipy.GRB.BINARY, name='y_'+str(i)))
    
        
    for i in key_list:
        ngh = adj[i]
        ngh_list = [] # collecting the corresponding x's
        for n in ngh:
            ngh_list.append(x[all_ele.index(n)])
        m.addConstr(y[i] >= (1/len(ngh_list))* gurobipy.quicksum(ngh_list))
            #bounds y[i] 
        m.addConstr(y[i] <= gurobipy.quicksum(ngh_list))
            #makes sure y[i] is 0 (not covered) if all elements in ngh_list are zero (not chosen)
       
    k = 2   #max nodes you can choose
    m.addConstr(gurobipy.quicksum(x) <= k) #limits # nodes chosen to k
       
    m.update()
    
    m.setObjective(gurobipy.quicksum(y), gurobipy.GRB.MAXIMIZE)
    #m.setObjective(quicksum( pop[j]*r[j] for j in range(numR) ), GRB.MAXIMIZE)
    
    m.optimize()
    
    #print(y)
    chosen = []
    for v in y:
        if v.X == 1: # to check if it was chosen or not        
            name = v.varName.split("_")
            index = int(name[1])
           # print(index)
            chosen.append(all_ele[index])
    
  # print(gurobipy.quicksum(y))
            
    return chosen

print(mostCovered(adj))

