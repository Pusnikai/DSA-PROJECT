# DSA-PROJECT

Background:
The transition to Electric Vehicles (EVs) is a critical step towards reducing global carbon
emissions. However, the effectiveness of this transition is heavily reliant on the accessibility and
efficiency of EV charging infrastructure. This project focuses on leveraging algorithmic solutions
to optimize route planning for EV users, making the process of locating and navigating to the
nearest or most convenient charging station as seamless as possible.

Project Details:
The goal is to develop an application that, given a starting point in a network of 23 nodes (including
4 charging stations), finds the shortest path to each charging station and recommends the most
efficient route based on distance and other relevant factors.

1. Graph Construction and Data Loading:
• Load a predefined network of nodes and edges from an external file (get data from the given image).
• Construct a graph representing the network, with nodes and weighted edges indicating distances.

2. Routing Algorithm Implementation:
• Implement Dijkstra's algorithm to determine the shortest path from the starting node to each charging station. This will show all the possible shortest paths for all four-charging station from a starting point (E.g., Node A)

3. Route Recommendation System:
• Analyze the computed paths to recommend the most efficient route to a charging station based on total distance