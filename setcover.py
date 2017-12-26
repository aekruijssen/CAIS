# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:36:37 2017

@author: adina
"""

from gurobipy import *
adj = {} # dict in python
filehandle=open("sim_graph_barabasi.txt", "r")

for line in filehandle.readlines():
    current_line = line.split(":")
    node = int(current_line[0])
    to_split = current_line[1]
    ngh = [int(x) for x in to_split.split(",")]
    adj[node]=ngh
    
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
    return all_elements

def setcover(adj):
    key_list = [x for x in adj.keys()]
    all_ele = get_all_elements(adj)
    m = gurobipy.Model()
    x = []
    for i in range(0, len(all_ele)):
        x.append(m.addVar(vtype=gurobipy.GRB.BINARY, name='x_'+str(i)))
        
    for i in key_list:
        ngh = adj[i]
        ngh_list = [] # collecting the corresponding x's
        for n in ngh:
            ngh_list.append(x[all_ele.index(n)])
        m.addConstr(gurobipy.quicksum(ngh_list)>=1)
        
    m.update()
    
    m.setObjective(gurobipy.quicksum(x),gurobipy.GRB.MINIMIZE)
    
    m.optimize()
    
    chosen = []
    for v in m.getVars():
        if v.x == 1: # to check if it was chosen or not        
            name = v.varName.split("_")
            index = int(name[1])
            chosen.append(key_list[index])
            
    return chosen

print(setcover(adj))



        
        
        
