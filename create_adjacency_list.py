from utils.create_graph import create_graph

def create_adjacency_list():
    """
    Create an adjacency list representation of the street grid graph.
    
    Returns:
        dict: Dictionary where keys are vertex indices and values are lists of 
              tuples (neighbor_vertex, edge_weight)
    """
    
    # Get the graph data
    edges, vertices = create_graph()
    
    # Initialize adjacency list
    adj_list = {}
    
    # Initialize empty lists for all vertices
    for vertex_index, row, col in vertices:
        adj_list[vertex_index] = []
    
    # Add edges to adjacency list (undirected graph)
    for start, end, weight in edges:
        adj_list[start].append((end, weight))
        adj_list[end].append((start, weight))
    
    return adj_list

def print_adjacency_list(adj_list, max_vertices_to_show=10):
    """
    Print the adjacency list in a readable format.
    
    Args:
        adj_list (dict): The adjacency list
        max_vertices_to_show (int): Maximum number of vertices to display
    """
    
    print("Adjacency List Representation:")
    print("=" * 50)
    print("Format: vertex_index: [(neighbor, weight), ...]")
    print("=" * 50)
    
    vertex_count = 0
    for vertex in sorted(adj_list.keys()):
        if vertex_count >= max_vertices_to_show:
            print(f"... (showing first {max_vertices_to_show} vertices)")
            break
            
        neighbors = sorted(adj_list[vertex])
        print(f"{vertex}: {neighbors}")
        vertex_count += 1
    
    print(f"\nTotal vertices: {len(adj_list)}")
    print(f"Graph statistics:")
    
    # Calculate some statistics
    total_edges = sum(len(neighbors) for neighbors in adj_list.values()) // 2
    print(f"Total edges: {total_edges}")
    
    # Count vertices by degree
    degree_counts = {}
    for vertex, neighbors in adj_list.items():
        degree = len(neighbors)
        degree_counts[degree] = degree_counts.get(degree, 0) + 1
    
    print(f"Degree distribution:")
    for degree in sorted(degree_counts.keys()):
        print(f"  Degree {degree}: {degree_counts[degree]} vertices")

def save_adjacency_list(adj_list, filename="adjacency_list.txt"):
    """
    Save the adjacency list to a text file.
    
    Args:
        adj_list (dict): The adjacency list
        filename (str): Output filename
    """
    
    with open(filename, 'w') as f:
        f.write("Adjacency List for 20x10 Street Grid Graph\n")
        f.write("=" * 50 + "\n")
        f.write("Format: vertex_index: [(neighbor, weight), ...]\n")
        f.write("=" * 50 + "\n\n")
        
        for vertex in sorted(adj_list.keys()):
            neighbors = sorted(adj_list[vertex])
            f.write(f"{vertex}: {neighbors}\n")
        
        f.write(f"\nTotal vertices: {len(adj_list)}\n")
        total_edges = sum(len(neighbors) for neighbors in adj_list.values()) // 2
        f.write(f"Total edges: {total_edges}\n")
    
    print(f"Adjacency list saved to {filename}")

if __name__ == "__main__":
    # Create the adjacency list
    adj_list = create_adjacency_list()
    
    # Print a sample of the adjacency list
    print_adjacency_list(adj_list, max_vertices_to_show=20)
    
    # Save the complete adjacency list to a file
    save_adjacency_list(adj_list)
    
    # Show some example vertices and their neighbors
    print("\nExample vertices and their neighbors:")
    print("-" * 40)
    
    # Corner vertices
    corner_vertices = [0, 19, 180, 199]  # Top-left, Top-right, Bottom-left, Bottom-right
    for vertex in corner_vertices:
        neighbors = adj_list[vertex]
        print(f"Vertex {vertex} (corner): {neighbors}")
    
    # Center vertex
    center_vertex = 5 * 20 + 10  # Middle of the grid
    neighbors = adj_list[center_vertex]
    print(f"Vertex {center_vertex} (center): {neighbors}")
