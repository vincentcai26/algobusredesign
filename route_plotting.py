import matplotlib.pyplot as plt
import networkx as nx

def plot_routes_on_graph(vertices, edges, routes_list, figsize=(15, 8)):
    """
    Plot routes on the graph.
    
    Args:
        vertices: List of vertices from create_graph()
        edges: List of edges from create_graph()
        routes_list: List of routes, where each route is a list of vertex indices in order
        figsize: Figure size tuple
    """
    # Create NetworkX graph
    G = nx.Graph()
    
    # Add vertices with positions
    pos = {}
    for vertex_id, row, col in vertices:
        G.add_node(vertex_id)
        pos[vertex_id] = (col, -row)  # Negative row for proper orientation
    
    # Add edges
    for start, end, weight in edges:
        G.add_edge(start, end, weight=weight)
    
    # Create plot
    plt.figure(figsize=figsize)
    
    # Draw all edges in light gray
    nx.draw_networkx_edges(G, pos, edge_color='lightgray', width=0.5, alpha=0.7)
    
    # Draw all nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=20, alpha=0.8)
    
    # Draw routes if provided
    if routes_list:
        colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
        
        for i, route in enumerate(routes_list):
            if len(route) < 2:
                continue
                
            color = colors[i % len(colors)]
            
            # Draw route edges
            route_edges = [(route[j], route[j+1]) for j in range(len(route)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=route_edges, 
                                 edge_color=color, width=3, alpha=0.8)
            
            # Highlight start and end nodes
            nx.draw_networkx_nodes(G, pos, nodelist=[route[0]], 
                                 node_color=color, node_size=100, alpha=1.0, 
                                 node_shape='s')  # Square for start
            nx.draw_networkx_nodes(G, pos, nodelist=[route[-1]], 
                                 node_color=color, node_size=100, alpha=1.0, 
                                 node_shape='^')  # Triangle for end
    
    plt.title('Street Grid Graph with Routes')
    plt.axis('equal')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_single_route(vertices, edges, route, title="Route Visualization"):
    """
    Plot the graph with a single route highlighted.
    
    Args:
        vertices: List of vertices from create_graph()
        edges: List of edges from create_graph()
        route: List of vertex indices in order
        title: Plot title
    """
    plot_routes_on_graph(vertices, edges, [route])
    plt.title(title)