import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes with labels (exact match to patent, all improvements)
nodes = [
    "1. User Requests to Play Content",
    "2. Is Adaptive Security Active?",
    "3. Is Token Valid?",
    "4. Is Environment Secure?",
    "5. Decrypt and Start Playback",
    "6. Embed Forensic Watermark",
    "7. Log Session to Encrypted Audit Logs",
    "8. Monitor for Real-Time Leaks",
    "9. Leak Detected?",
    "10. DRM Compatibility Layer",
    "11. Session Ends or Playback Completes",
    "Deny Access & Log the Incident",
    "Enforcement Procedure"
]

for node in nodes:
    G.add_node(node)

# Add edges with labels (all improvements: exact "Yes/No", "Continue" for sequential, no clutter)
G.add_edge("1. User Requests to Play Content", "2. Is Adaptive Security Active?", label="Start")
G.add_edge("2. Is Adaptive Security Active?", "3. Is Token Valid?", label="Yes/No (proceed)")
G.add_edge("3. Is Token Valid?", "4. Is Environment Secure?", label="Yes")
G.add_edge("3. Is Token Valid?", "Deny Access & Log the Incident", label="No")
G.add_edge("4. Is Environment Secure?", "5. Decrypt and Start Playback", label="Yes")
G.add_edge("4. Is Environment Secure?", "Deny Access & Log the Incident", label="No")
G.add_edge("5. Decrypt and Start Playback", "6. Embed Forensic Watermark", label="Continue")
G.add_edge("6. Embed Forensic Watermark", "7. Log Session to Encrypted Audit Logs", label="Continue")
G.add_edge("7. Log Session to Encrypted Audit Logs", "8. Monitor for Real-Time Leaks", label="Continue")
G.add_edge("8. Monitor for Real-Time Leaks", "9. Leak Detected?", label="Continue")
G.add_edge("9. Leak Detected?", "Enforcement Procedure", label="Yes")
G.add_edge("9. Leak Detected?", "10. DRM Compatibility Layer", label="No")
G.add_edge("10. DRM Compatibility Layer", "11. Session Ends or Playback Completes", label="Continue")

# Draw the graph (B&W USPTO-style: black edges/text, white nodes; high-res; clean layout)
pos = nx.spring_layout(G, seed=42)  # Consistent balanced layout
plt.figure(figsize=(12, 8), dpi=300)  # High-res for printing
nx.draw(G, pos, with_labels=True, node_color="white", edge_color="black", node_size=3000, font_size=8, font_weight="bold", arrowsize=20, font_color="black")
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u,v): d.get('label', '') for u,v,d in G.edges(data=True)}, font_color="black", font_size=8)
plt.title("Figure 1 – System Logic Flow Diagram for VisualKey")
plt.axis("off")
plt.savefig("visualkey_flow_diagram.png", bbox_inches='tight', pad_inches=0.1, facecolor='white')  # Optimized save for download
plt.show()  # Display if running locally; otherwise, just save the file
