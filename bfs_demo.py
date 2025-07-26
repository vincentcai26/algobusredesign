"""
BFS Demo Script

This script demonstrates the breadth-first search function to find distances
from randomly generated start and end points to all vertices in the graph.

The output is a list where:
- At index i: there is another list representing vertex i
- At index j of that list: there is a tuple (distance_from_start_j, distance_from_end_j)
"""

from distance_analysis import calculate_distances_to_all_vertices, generate_random_point_pairs
from utils.create_graph import create_graph

def main():
    print("=== BFS Distance Calculation Demo ===\n")
    
    # Create the graph from test.ipynb
    print("Creating the 20x10 street grid graph...")
    edges, vertices = create_graph()
    print(f"Graph created with {len(vertices)} vertices and {len(edges)} edges\n")
    
    # Generate random point pairs (you can change the number as needed)
    n_pairs = 3  # Using 3 pairs for demonstration
    print(f"Generating {n_pairs} random point pairs...")
    random_pairs = generate_random_point_pairs(n_pairs, seed=42)
    
    print("Random point pairs generated:")
    for i, (start, end) in enumerate(random_pairs):
        print(f"  Pair {i}: Start vertex {start}, End vertex {end}")
    
    # Calculate distances using BFS
    print(f"\nCalculating distances using BFS...")
    distance_matrix = calculate_distances_to_all_vertices(random_pairs, edges)
    
    print("Distance calculation complete!\n")
    
    # Show the structure of the result
    print("=== Result Structure ===")
    print("distance_matrix[i][j] = (distance from start_j to vertex_i, distance from end_j to vertex_i)")
    print(f"Total vertices: {len(distance_matrix)}")
    print(f"Total pairs: {len(random_pairs)}")
    print()
    
    # Show detailed examples for first few vertices
    print("=== Detailed Examples ===")
    for i in range(min(10, len(distance_matrix))):
        print(f"Vertex {i}:")
        for j in range(len(random_pairs)):
            dist_from_start, dist_from_end = distance_matrix[i][j]
            start_vertex, end_vertex = random_pairs[j]
            print(f"  Pair {j} (Start: {start_vertex}, End: {end_vertex}): "
                  f"Distance from start = {dist_from_start}, Distance from end = {dist_from_end}")
        print()
    
    # Show how to access specific information
    print("=== Usage Examples ===")
    
    # Example 1: Get distances from vertex 50 to all pairs
    vertex_50_distances = distance_matrix[50]
    print(f"Distances from vertex 50 to all start/end pairs:")
    for j, (dist_start, dist_end) in enumerate(vertex_50_distances):
        print(f"  Pair {j}: Distance to start = {dist_start}, Distance to end = {dist_end}")
    print()
    
    # Example 2: Get distance from a specific pair to a specific vertex
    specific_vertex = 100
    specific_pair = 1
    dist_to_start, dist_to_end = distance_matrix[specific_vertex][specific_pair]
    print(f"Distance from vertex {specific_vertex} to pair {specific_pair}:")
    print(f"  To start vertex {random_pairs[specific_pair][0]}: {dist_to_start}")
    print(f"  To end vertex {random_pairs[specific_pair][1]}: {dist_to_end}")
    print()
    
    # Example 3: Find vertices closest to a specific start point
    pair_to_analyze = 0
    print(f"Finding vertices closest to start point of pair {pair_to_analyze} (vertex {random_pairs[pair_to_analyze][0]}):")
    vertices_with_distances = [(i, distance_matrix[i][pair_to_analyze][0]) for i in range(len(distance_matrix))]
    vertices_with_distances.sort(key=lambda x: x[1])
    
    print("Top 5 closest vertices:")
    for i, (vertex, distance) in enumerate(vertices_with_distances[:5]):
        print(f"  {i+1}. Vertex {vertex}: Distance = {distance}")
    
    print(f"\nData structure summary:")
    print(f"- distance_matrix is a list of {len(distance_matrix)} lists (one for each vertex)")
    print(f"- Each inner list has {len(random_pairs)} tuples (one for each pair)")
    print(f"- Each tuple contains (distance_from_start_j, distance_from_end_j)")
    print(f"- Access pattern: distance_matrix[vertex_i][pair_j] = (dist_from_start_j, dist_from_end_j)")
    
    return distance_matrix, random_pairs

if __name__ == "__main__":
    distance_matrix, random_pairs = main()
