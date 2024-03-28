'''
INFR 2820U: Algorithm and Data Structures
Group Project
Prashanth Baskaran Nallathamby 100784991
Sangeethan Thevathasan 100867103
Ayaan Bajwa 100864399

'''

import csv
import networkx as nx
import matplotlib.pyplot as plt


def load_csv(filepath):
    Graph = nx.Graph()
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            source = row['Node']
            target = row['Edge']
            distance = int(row['Distance'])
            Graph.add_edge(source, target, weight=distance)
    return Graph


def Display_Graph(Graph):
    pos = nx.spring_layout(Graph)
    nx.draw_networkx(Graph)
    plt.show()
    
    
filepath = 'data.csv'
Graph = load_csv(filepath)
Display_Graph(Graph)
print('Nodes: ', Graph.nodes())
print('Edges: ',Graph.edges())


    