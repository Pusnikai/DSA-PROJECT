# DSA-PROJECT

## Setup Instructions

1. **Install Python:**
   - Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries:**
   - Open a terminal or command prompt and run the following command:
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
   - Run the Python script by executing the following command:
     ```
     python Project.py
     ```

3. **Follow the Prompts:**
   - Enter the current point (between A to W) when prompted.
   - The script will display the graph with charging stations highlighted and recommend the most efficient route considering the shortest distance to the stations.

## Code Quality and Documentation

1. **Code Quality:**
   - Variable and function names: Use meaningful and descriptive names to enhance readability.
   - Comments: Add comments to explain complex logic, algorithms, or any parts of the code that might not be immediately clear to others.
   - Error handling: Implement error handling to handle unexpected situations gracefully.

2. **Documentation:**
   - Add a docstring to each function explaining its purpose, parameters, and return values. This will make it easier for others (and yourself) to understand the code's functionality.
   - Provide inline comments to explain key sections of the code, especially complex logic or algorithms.



# Efficient Route Finder

This application aims to find the shortest path from a given starting point to each charging station in a network of 23 nodes, and recommend the most efficient route based on distance and other relevant factors.

## Project Details

### 1. Graph Construction and Data Loading:
- Load a predefined network of nodes and edges from an external file (get data from the given image).
- Construct a graph representing the network, with nodes and weighted edges indicating distances.

### 2. Routing Algorithm Implementation:
- Implement Dijkstra's algorithm to determine the shortest path from the starting node to each charging station. This will show all the possible shortest paths for all four charging stations from a starting point (e.g., Node A).

### 3. Route Recommendation System:
- Analyze the computed paths to recommend the most efficient route to a charging station based on total distance.
