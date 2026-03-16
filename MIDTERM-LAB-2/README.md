Cavite Route Network - Path Finder
An interactive web-based navigation tool designed to find the most efficient routes between key locations in Cavite. The application supports multi-criteria optimization, allowing users to find paths based on distance, time, or fuel consumption.

🚀 Features
Dijkstra's Algorithm: Implements the classic greedy algorithm to ensure the mathematically shortest path is always found.

Multi-Metric Optimization: Switch between three different cost factors:

📏 Distance: Total kilometers traveled.

⏱️ Time: Estimated travel time in minutes.

⛽ Fuel: Calculated fuel consumption in liters.

Interactive Visualization: A dynamic HTML5 Canvas that displays the network graph, highlights the optimal route, and shows alternative paths.

Alternative Route Generation: Uses an edge-removal strategy to find and display up to three secondary route options.

User Controls: Swap start/end points, zoom in/out of the map, and pan across the network.

🧠 Approach & Algorithm
1. Data Representation (The Graph)
The network is modeled as a weighted undirected graph.

Nodes: Represent cities/towns (e.g., Imus, Bacoor, Dasmariñas).

Edges: Represent the roads connecting them. Each edge is an object containing multiple weights: distance, time, and fuel.

2. Pathfinding Logic
The core of the application is Dijkstra’s Algorithm. The process follows these steps:

Initialize all node distances to infinity, except the starting node which is set to 0.

Store all nodes in an "unvisited" set.

While unvisited nodes exist:

Select the node with the smallest distance.

For each neighbor of the current node, calculate the cumulative distance (or time/fuel) through the current node.

If this new path is shorter than the previously known distance, update the neighbor's distance and record the current node as its "parent."

Once the destination is reached, backtrack through the "parents" to reconstruct the final path.

3. Alternative Paths
To provide users with more than one option, the application utilizes a variation of the Yen’s Algorithm concept. It identifies the "shortest" path, then temporarily removes edges from that path and re-runs Dijkstra to find the next best available route.

🛠️ Technical Stack
HTML5: Structure and Canvas for the map rendering.

CSS3: Modern "Glassmorphism" dashboard design using Flexbox and Grid.

Vanilla JavaScript: Pure logic for graph traversal and UI interactions (no external libraries required).

🚧 Challenges Faced
Bidirectional Consistency
One challenge was ensuring the graph behaved correctly as an undirected network. Initially, paths only worked in one direction. This was solved by creating an adjacency list that automatically mirrors every edge entry (e.g., if Imus connects to Bacoor, Bacoor is programmatically updated to connect back to Imus with identical weights).

Map Scaling & Panning
Rendering a static map is simple, but making it interactive on a Canvas required complex coordinate transformations. Implementing a transformPoint function was necessary to map the raw node coordinates to the current zoom level and offset (X, Y) determined by the user's mouse dragging.

Path Reconstruction
Dijkstra's algorithm only tells you the cost to get to a node. To show the actual list of cities (IMUS → BACOOR → SILANG), I had to implement a previous node tracker that stores the history of the traversal, allowing the code to "trace its steps" backward from the destination.