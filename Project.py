'''
INFR 2820U: Algorithm and Data Structures
Group Project
Prashanth Baskaran Nallathamby 100784991
Sangeethan Thevathasan 100867103
Ayaan Bajwa 100864399
Abishan Jeyanathan 
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

def Display_Graph(Graph,Node_Label):
    pos = nx.spring_layout(Graph)
    nx.draw_networkx_nodes(Graph, pos, node_color=Node_Label)
    nx.draw_networkx_edges(Graph,pos)
    nx.draw_networkx_labels(Graph, pos)
    edge_labels = {(Start,Next): weight['weight'] for Start, Next, weight in Graph.edges(data=True)}
    nx.draw_networkx_edge_labels(Graph, pos, edge_labels=edge_labels)
    plt.show()
    
def IsChargingStation(Graph, stations):
    
    Node_Label = []
    for node in Graph.nodes():
        if node not in stations:
            Node_Label.append('lightgrey')
        else:
            Node_Label.append('lightgreen')
            
    return Node_Label          
    
def DijkstraRouting(Graph, origin, station):
    Visit = {node: False for node in Graph.nodes()}
    distance = {node:float('inf')for node in Graph.nodes()}
    path = {node:None for node in Graph.nodes()}
    distance[origin] = 0
    
    while not Visit[station]:
        minDist = float('inf')
        minNode = None
        for node in Graph.nodes():
            if not Visit[node] and distance[node] < minDist:
                minDist = distance[node]
                minNode = node
                
        Visit[minNode] = True
        
        for neighbor in Graph.neighbors(minNode):
            if not Visit[neighbor]:
                newDistance = distance[minNode] + Graph[minNode][neighbor]['weight']
                if newDistance < distance[neighbor]:
                    distance[neighbor] = newDistance
                    path[neighbor] = minNode
    
    PathToGoal = []
    TotalDist = [distance[station]]
    actualNode = station
    while actualNode != origin:
        PathToGoal.insert(0,actualNode)
        actualNode = path[actualNode]
    PathToGoal.insert(0,origin)    
      
    return PathToGoal, TotalDist
    
def EfficientRoute(Graph,origin,stations):
    optimal = []
    for station in stations:
        path, dist = DijkstraRouting(Graph,origin,station)
        print("\nThe shortest route from {} to {}: ".format(origin,station),path)
        print('Total Distance is :',dist)
        optimal.append( (path, dist) )
    optimal.sort(key=lambda x:x[1]) 
    ShortestPath,ShortestDist   = optimal[0]
    print('\nThe Recommended Station Route is : ',ShortestPath)
    print('Total Distance: ',ShortestDist)
        
     
        
    
def main():   
    filepath = 'data.csv'
    Graph = load_csv(filepath)
    stations = ['H','K','Q','T']
    Label = IsChargingStation(Graph,stations)
    Display_Graph(Graph,Label)
    origin  = input("\nEnter the current point (Between A to W): ")
    EfficientRoute(Graph,origin,stations)
   
    
    #print('\nNodes: ', Graph.nodes())
    #print('\nEdges: ',Graph.edges())
    #print('\nWeight: ',[(u, v, d['weight']) for u, v, d in Graph.edges(data=True)])

main()
    