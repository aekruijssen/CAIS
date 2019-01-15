# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:02:22 2018

@author: adina
"""

adj = {} # dict in python
filehandle=open("sim_graph_barabasi.txt", "r")

for line in filehandle.readlines():
    current_line = line.split(":")
    node = int(current_line[0])
    to_split = current_line[1]
    ngh = [int(x) for x in to_split.split(",")] #array of a node's neighbors
    adj[node]=ngh # array of each node's neighbors array (array of arrays)
    for n in adj:
        for n1 in ngh:
            if n not in adj[n1]:
                adj[n1].append(n)
                #or?
                #ngh.append(n1)
    
#print(adj)
#print('num of elements', len(adj.keys()))

def get_all_elements(adj):
    
    max1 = 0
    max2 = 0
    all_elements = []
    for e in adj:
        if e not in all_elements:
            all_elements.append(e)
        neighbours = adj[e]
        for e1 in neighbours:
            if e1 not in all_elements:
                all_elements.append(e1)
            #if e not in adj[e1]:      
            #print(e1)
                
            
    print (node1)
    print ("# neighbors: ")
    print (max1)
    print ("  ")
    print (node2)
    print ("# neighbors: ")
    print (max2)
            
    return all_elements #array of each node (ex: [1, 2, 3, ...])

def mostCovered(adj):
    key_list = [x for x in adj.keys()]
    #print(key_list)
    all_ele = get_all_elements(adj)
        
    for i in key_list:
        ngh = adj[i]
        ngh_list = [] # collecting the corresponding x's
        for n in ngh:
            #ngh_list.append(x[all_ele.index(n)])
            if i not in ngh_list:
                ngh_list.append()

#print(get_all_elements(adj))