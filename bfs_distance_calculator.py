from collections import deque, defaultdict
import random
from utils.create_graph import create_graph

def build_adjacency_list(edges):
    """
    Build an adjacency list representation of the graph from the edges.
    
    Args:
        edges: List of tuples (start, end, weight)
    
    Returns:
        dict: Adjacency list where keys are vertices and values are lists of (neighbor, weight) tuples
    """
    adj_list = defaultdict(list)
    
    for start, end, weight in edges:
        adj_list[start].append((end, weight))
        adj_list[end].append((start, weight))
    
    return adj_list

def bfs_shortest_distances(adj_list, start_vertex, total_vertices):
    """
    Use BFS to find shortest distances from start_vertex to all other vertices.
    
    Args:
        adj_list: Adjacency list representation of the graph
        start_vertex: Starting vertex
        total_vertices: Total number of vertices in the graph
    
    Returns:
        list: distances[i] = shortest distance from start_vertex to vertex i
    """
    distances = [float('inf')] * total_vertices
    distances[start_vertex] = 0
    
    queue = deque([start_vertex])
    
    while queue:
        current = queue.popleft()
        
        for neighbor, weight in adj_list[current]:
            new_distance = distances[current] + weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                queue.append(neighbor)
    
    return distances

def generate_random_point_pairs(n, total_vertices=200):
    """
    Generate n random sets of two points (start and end) at vertices on the grid.
    
    Args:
        n (int): Number of random point pairs to generate
        total_vertices (int): Total number of vertices in the grid (default: 200)
    
    Returns:
        list: List of tuples, each containing (start_vertex, end_vertex)
    """
    point_pairs = []
    
    for i in range(n):
        # Generate two different random vertices
        start_vertex = random.randint(0, total_vertices - 1)
        end_vertex = random.randint(0, total_vertices - 1)
        
        # Ensure start and end are different
        while end_vertex == start_vertex:
            end_vertex = random.randint(0, total_vertices - 1)
        
        point_pairs.append((start_vertex, end_vertex))
    
    return point_pairs

def calculate_distances_to_all_vertices(random_pairs, edges, total_vertices=200):
    """
    Calculate distances from every vertex to all start and end points in random_pairs.
    
    Args:
        random_pairs: List of (start_vertex, end_vertex) tuples
        edges: List of edges in the graph
        total_vertices: Total number of vertices in the graph
    
    Returns:
        list: result[i][j] = (distance from start_j to vertex_i, distance from end_j to vertex_i)
    """
    # Build adjacency list
    adj_list = build_adjacency_list(edges)
    
    # Initialize result structure
    result = [[None for _ in range(len(random_pairs))] for _ in range(total_vertices)]
    
    # For each random pair, calculate distances from start and end to all vertices
    for j, (start_vertex, end_vertex) in enumerate(random_pairs):
        print(f"Processing pair {j+1}/{len(random_pairs)}: Start {start_vertex}, End {end_vertex}")
        
        # Calculate distances from start vertex to all vertices
        distances_from_start = bfs_shortest_distances(adj_list, start_vertex, total_vertices)
        
        # Calculate distances from end vertex to all vertices
        distances_from_end = bfs_shortest_distances(adj_list, end_vertex, total_vertices)
        
        # Store results for all vertices
        for i in range(total_vertices):
            result[i][j] = (distances_from_start[i], distances_from_end[i])
    
    return result

def main():
    """
    Main function to demonstrate the distance calculation functionality.
    """
    print("Creating graph...")
    edges, vertices = create_graph()
    
    print(f"\nGraph created with {len(vertices)} vertices and {len(edges)} edges")
    
    # Generate random point pairs
    n_pairs = 5
    print(f"\nGenerating {n_pairs} random point pairs...")
    random_pairs = generate_random_point_pairs(n_pairs)
    
    print(f"\nGenerated {n_pairs} random point pairs:")
    for i, (start, end) in enumerate(random_pairs, 1):
        print(f"Pair {i}: Start vertex {start}, End vertex {end}")
    
    # Calculate distances
    print(f"\nCalculating distances from all vertices to start and end points...")
    distance_matrix = calculate_distances_to_all_vertices(random_pairs, edges)
    
    print(f"\nDistance calculation complete!")
    print(f"Result structure: distance_matrix[vertex_i][pair_j] = (distance_from_start_j, distance_from_end_j)")
    
    # Show some example results
    print(f"\nExample results for first 5 vertices:")
    for i in range(min(5, len(distance_matrix))):
        print(f"Vertex {i}:")
        for j in range(len(random_pairs)):
            dist_from_start, dist_from_end = distance_matrix[i][j]
            print(f"  Pair {j+1}: Distance from start {random_pairs[j][0]} = {dist_from_start}, "
                  f"Distance from end {random_pairs[j][1]} = {dist_from_end}")
    
    return distance_matrix, random_pairs

if __name__ == "__main__":
    distance_matrix, random_pairs = main()
