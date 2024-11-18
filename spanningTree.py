import networkx as nx

# Create a graph for the electrical grid
G = nx.Graph()

# Add edges (connections) with weights (costs)
# Format: (city1, city2, cost)
edges = [
    ("CityA", "CityB", 4),
    ("CityA", "CityC", 2),
    ("CityB", "CityC", 5),
    ("CityB", "CityD", 10),
    ("CityC", "CityD", 3),
    ("CityC", "CityE", 7),
    ("CityD", "CityE", 1)
]

# Add edges to the graph
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Compute the minimum spanning tree using Kruskal's algorithm
mst = nx.minimum_spanning_tree(G, algorithm="kruskal")

# Display the edges of the MST
print("Edges in the Minimum Spanning Tree with costs:")
for u, v, data in mst.edges(data=True):
    print(f"{u} - {v}: {data['weight']}")
