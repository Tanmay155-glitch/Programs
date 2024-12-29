# Import necessary libraries
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import girvan_newman
import csv

# Step 1: Input Data Preparation
# Read the data from a CSV file into a graph using NetworkX
filename = "social_network_edges.csv"  # Replace with your CSV file path
data = pd.read_csv(filename)

# Initialize an undirected graph
G = nx.from_pandas_edgelist(data, source='Source', target='Target')

# Step 2: Graph Construction
# Display basic statistics
print("Graph Statistics:")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
degree_distribution = dict(G.degree())
print("Degree Distribution:", degree_distribution)

# Step 3: Centrality Analysis
# Compute centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

# Save centrality scores to a CSV file
centrality_scores = pd.DataFrame({
    'Node': list(degree_centrality.keys()),
    'Degree Centrality': list(degree_centrality.values()),
    'Betweenness Centrality': list(betweenness_centrality.values()),
    'Closeness Centrality': list(closeness_centrality.values())
})
centrality_scores.to_csv('centrality_scores.csv', index=False)

# Plot degree centrality
plt.figure(figsize=(8, 6))
plt.bar(degree_centrality.keys(), degree_centrality.values(), color='skyblue')
plt.title("Degree Centrality")
plt.xlabel("Nodes")
plt.ylabel("Centrality Score")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Step 4: Community Detection
# Apply the Girvan-Newman community detection algorithm
communities = list(girvan_newman(G))
top_level_communities = tuple(sorted(c) for c in next(iter(communities)))
print("Detected Communities:", top_level_communities)

# Assign community labels to nodes
community_dict = {node: idx + 1 for idx, community in enumerate(top_level_communities) for node in community}

# Save community assignments to a CSV file
with open('community_assignments.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Node', 'Community'])
    for node, community in community_dict.items():
        writer.writerow([node, community])

# Step 5: Visualization
# Visualize the graph with nodes sized by degree centrality and colored by community
plt.figure(figsize=(10, 8))

# Create a color map for communities
colors = [community_dict[node] for node in G.nodes()]
sizes = [5000 * degree_centrality[node] for node in G.nodes()]

nx.draw(
    G,
    with_labels=True,
    node_color=colors,
    node_size=sizes,
    cmap=plt.cm.viridis,
    font_size=8,
    edge_color="gray"
)

plt.title("Social Network Graph with Communities")
plt.show()

# Output complete
print("Analysis complete. Centrality scores and community assignments saved to CSV files.")
