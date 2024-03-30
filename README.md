# DSA-PROJECT

## Overview

This project aims to facilitate efficient route finding within a network of charging stations for Electric Vehicles (EVs). It utilizes graph theory principles and Dijkstra's algorithm to determine the shortest path from a given starting point to each charging station, offering recommendations for the most efficient route based on distance and other relevant factors.

## Setup Instructions

1. **Install Python:**
   - Ensure Python is installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries:**
   - Open a terminal or command prompt and run:
     ```
     pip install networkx matplotlib
     ```

3. **Download Data File:**
   - Save your CSV data file (`data.csv`) in the same directory as your Python script.

## Execution Instructions

1. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing your Python script (`Project.py`) and the CSV data file.

2. **Execute the Script:**
   - Run the Python script:
     ```
     python Project.py
     ```

3. **Follow the Prompts:**
   - Enter the current point (between A to W) when prompted.
   - The script will display the graph with charging stations highlighted and recommend the most efficient route considering the shortest distance to the stations.

## Features

- **Graph Construction:** Constructs a weighted directed graph from the provided data file, representing nodes and edges with distances.
- **Routing Algorithm:** Implements Dijkstra's algorithm to find the shortest path from the starting node to each charging station.
- **Route Recommendation:** Analyzes computed paths to recommend the most efficient route to a charging station based on total distance.
- **Graph Visualization:** Utilizes NetworkX and Matplotlib to visualize the network graph, highlighting charging stations for better understanding.
- **User Interaction:** Provides a user-friendly interface prompting for the current node and displaying recommended routes.

## Project Logs

1. **Data Preparation:**
   - Recorded node and edge information, along with distances between nodes.
   - Created a CSV file to represent the network data.
   - Loaded CSV data for interpretation in Python.

2. **Graph Visualization:**
   - Utilized NetworkX and Matplotlib libraries to visualize the graph.
   - Differentiated charging stations with distinct colors for clarity.
   - Labeled edge attributes, such as weight (distance), for better comprehension.

3. **Dijkstra's Algorithm Implementation:**
   - Implemented Dijkstra's algorithm to find the shortest path to each charging station from a given origin node.
   - Recorded paths, visited nodes, and distances traveled during iteration.
   - Calculated shortest distance and constructed the path to the charging station.

4. **Efficiency Calculation:**
   - Iterated through the list of EV stations to calculate the shortest path and total distance using Dijkstra's algorithm.
   - Recommended the shortest and nearest station based on calculated distances.

5. **Main Functionality:**
   - Executed the display function.
   - Prompted user input for the current node and displayed paths to each station, followed by recommending the best station to visit.

## Resources
- [NetworkX Documentation](https://networkx.org/documentation/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Python Tutorial on File Handling](http://www.pythonforbeginners.com/file-handling/reading-and-writing-files-in-python/)
- [Dijkstra’s Algorithm]()
- [Python Tutorial]()
-  [GeeksforGeeks]</s>

