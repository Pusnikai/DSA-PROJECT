'''
INFR 2820U: Algorithm and Data Structures
Group Project
Prashanth Baskaran Nallathamby 100784991
Sangeethan Thevathasan 100867103
Ayaan Bajwa 100864399
Abishan Jeyanathan 100790172
'''

# Importing Required Libraries
import csv
import networkx as nx
import matplotlib.pyplot as plt

# Reading the CSV file
def load_csv(filepath):
    Graph = nx.Graph()
    # Open the CSV File
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        # Adding nodes to the graph 
        for row in reader:
            source = row['Node']
            target = row['Edge']
            distance = int(row['Distance'])
            Graph.add_edge(source, target, weight=distance)
    return Graph

# Drawing the graph using NetworkX library
def Display_Graph(Graph,Node_Label):
    pos = nx.spring_layout(Graph)
    nx.draw_networkx_nodes(Graph, pos, node_color=Node_Label)
    nx.draw_networkx_edges(Graph,pos)
    nx.draw_networkx_labels(Graph, pos)
    edge_labels = {(Start,Next): weight['weight'] for Start, Next, weight in Graph.edges(data=True)}
    nx.draw_networkx_edge_labels(Graph, pos, edge_labels=edge_labels)
    plt.show()

# Checking if the Node iterating is a EV station or not
def IsChargingStation(Graph, stations):
    Node_Label = []
    # Iterate through each nodes of the graph
    for node in Graph.nodes():
        if node not in stations:
            Node_Label.append('lightgrey')
        else:
            Node_Label.append('lightgreen')      
    return Node_Label          

# Dijkstra's Algorithm Implementation
def DijkstraRouting(Graph, origin, station):
    # Creating a dictionary to store the shortest distances from
    Visit = {node: False for node in Graph.nodes()}
    distance = {node:float('inf')for node in Graph.nodes()}
    path = {node:None for node in Graph.nodes()}
    distance[origin] = 0
    # Loop for finding the shortest paths
    while not Visit[station]:
        minDist = float('inf')
        minNode = None
        # Finding the next node to visit
        for node in Graph.nodes():
            if not Visit[node] and distance[node] < minDist:
                minDist = distance[node]
                minNode = node   
        Visit[minNode] = True
        # ignore already visited nodes
        for neighbor in Graph.neighbors(minNode):
            if not Visit[neighbor]:
                newDistance = distance[minNode] + Graph[minNode][neighbor]['weight']
                if newDistance < distance[neighbor]:
                    distance[neighbor] = newDistance
                    path[neighbor] = minNode
    PathToGoal = []
    TotalDist = [distance[station]]
    actualNode = station
    # Building the path backwards
    while actualNode != origin:
        PathToGoal.insert(0,actualNode)
        actualNode = path[actualNode]
    PathToGoal.insert(0,origin)    
    return PathToGoal, TotalDist
 
#  Determining the Efficient Route and Displaying all the EV station Route
def EfficientRoute(Graph,origin,stations):
    optimal = []
    for station in stations:
        path, dist = DijkstraRouting(Graph,origin,station)
        print("\nThe shortest route from {} to {}: ".format(origin,station),path)
        print('Total Distance is :',dist)
        optimal.append( (path, dist) )
    # Returning the Optimal Station with minimum total distance
    optimal.sort(key=lambda x:x[1]) 
    ShortestPath,ShortestDist   = optimal[0]
    print('\nThe Recommended Station Route is : ',ShortestPath)
    print('Total Distance: ',ShortestDist)  

# Main Function
def main():   
    filepath = 'data.csv'
    Graph = load_csv(filepath)
    stations = ['H','K','Q','T']
    Label = IsChargingStation(Graph,stations)
    Display_Graph(Graph,Label)
    origin  = input("\nEnter the current point (Between A to W): ")
    EfficientRoute(Graph,origin,stations)
    """print('\nNodes: ', Graph.nodes())
    print('\nEdges: ',Graph.edges())
    print('\nWeight: ',[(u, v, d['weight']) for u, v, d in Graph.edges(data=True)])"""

# Calling the main function
if __name__ == "__main__":
    main()
    
    