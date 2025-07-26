"""
Distance Analysis Module

This module provides functions to calculate and analyze distances from randomly generated
start and end points to all vertices in the graph using breadth-first search.
"""

from collections import deque, defaultdict
import random
import numpy as np
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

def generate_random_point_pairs(n, total_vertices=200, seed=None):
    """
    Generate n random sets of two points (start and end) at vertices on the grid.
    
    Args:
        n (int): Number of random point pairs to generate
        total_vertices (int): Total number of vertices in the grid (default: 200)
        seed (int, optional): Random seed for reproducibility
    
    Returns:
        list: List of tuples, each containing (start_vertex, end_vertex)
    """
    if seed is not None:
        random.seed(seed)
    
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

def analyze_distance_statistics(distance_matrix, random_pairs):
    """
    Analyze statistical properties of the distance matrix.
    
    Args:
        distance_matrix: The distance matrix from calculate_distances_to_all_vertices
        random_pairs: List of (start_vertex, end_vertex) tuples
    
    Returns:
        dict: Statistics about the distances
    """
    stats = {
        'total_vertices': len(distance_matrix),
        'total_pairs': len(random_pairs),
        'pair_statistics': []
    }
    
    for j, (start_vertex, end_vertex) in enumerate(random_pairs):
        start_distances = [distance_matrix[i][j][0] for i in range(len(distance_matrix))]
        end_distances = [distance_matrix[i][j][1] for i in range(len(distance_matrix))]
        
        pair_stats = {
            'pair_index': j,
            'start_vertex': start_vertex,
            'end_vertex': end_vertex,
            'start_distances': {
                'min': min(start_distances),
                'max': max(start_distances),
                'mean': np.mean(start_distances),
                'std': np.std(start_distances)
            },
            'end_distances': {
                'min': min(end_distances),
                'max': max(end_distances),
                'mean': np.mean(end_distances),
                'std': np.std(end_distances)
            }
        }
        
        stats['pair_statistics'].append(pair_stats)
    
    return stats

def find_vertices_with_specific_properties(distance_matrix, random_pairs, property_func):
    """
    Find vertices that satisfy a specific property based on their distances.
    
    Args:
        distance_matrix: The distance matrix from calculate_distances_to_all_vertices
        random_pairs: List of (start_vertex, end_vertex) tuples
        property_func: Function that takes (vertex_index, distances_for_vertex) and returns bool
    
    Returns:
        list: List of vertex indices that satisfy the property
    """
    matching_vertices = []
    
    for i in range(len(distance_matrix)):
        distances_for_vertex = distance_matrix[i]
        if property_func(i, distances_for_vertex):
            matching_vertices.append(i)
    
    return matching_vertices

def get_closest_vertices_to_pair(distance_matrix, pair_index, n=5):
    """
    Get the n closest vertices to both start and end points of a specific pair.
    
    Args:
        distance_matrix: The distance matrix from calculate_distances_to_all_vertices
        pair_index: Index of the pair to analyze
        n: Number of closest vertices to return
    
    Returns:
        dict: Contains lists of closest vertices to start and end points
    """
    start_distances = [(i, distance_matrix[i][pair_index][0]) for i in range(len(distance_matrix))]
    end_distances = [(i, distance_matrix[i][pair_index][1]) for i in range(len(distance_matrix))]
    
    start_distances.sort(key=lambda x: x[1])
    end_distances.sort(key=lambda x: x[1])
    
    return {
        'closest_to_start': start_distances[:n],
        'closest_to_end': end_distances[:n]
    }

def main_analysis():
    """
    Main function to demonstrate the distance analysis functionality.
    """
    print("=== Distance Analysis for Street Grid Graph ===\n")
    
    # Create graph
    print("Creating graph...")
    edges, vertices = create_graph()
    print(f"Graph created with {len(vertices)} vertices and {len(edges)} edges\n")
    
    # Generate random point pairs with a seed for reproducibility
    n_pairs = 5
    print(f"Generating {n_pairs} random point pairs...")
    random_pairs = generate_random_point_pairs(n_pairs, seed=42)
    
    print(f"Generated {n_pairs} random point pairs:")
    for i, (start, end) in enumerate(random_pairs, 1):
        print(f"  Pair {i}: Start vertex {start}, End vertex {end}")
    
    # Calculate distances
    print(f"\nCalculating distances from all vertices to start and end points...")
    distance_matrix = calculate_distances_to_all_vertices(random_pairs, edges)
    
    print(f"Distance calculation complete!\n")
    
    # Analyze statistics
    print("=== Distance Statistics ===")
    stats = analyze_distance_statistics(distance_matrix, random_pairs)
    
    for pair_stats in stats['pair_statistics']:
        print(f"Pair {pair_stats['pair_index'] + 1} (Start: {pair_stats['start_vertex']}, End: {pair_stats['end_vertex']}):")
        print(f"  Distances from start: min={pair_stats['start_distances']['min']}, "
              f"max={pair_stats['start_distances']['max']}, "
              f"mean={pair_stats['start_distances']['mean']:.2f}")
        print(f"  Distances from end: min={pair_stats['end_distances']['min']}, "
              f"max={pair_stats['end_distances']['max']}, "
              f"mean={pair_stats['end_distances']['mean']:.2f}")
        print()
    
    # Find vertices closest to each pair
    print("=== Closest Vertices Analysis ===")
    for i in range(len(random_pairs)):
        closest = get_closest_vertices_to_pair(distance_matrix, i, n=3)
        print(f"Pair {i+1} closest vertices:")
        print(f"  Closest to start {random_pairs[i][0]}: {closest['closest_to_start']}")
        print(f"  Closest to end {random_pairs[i][1]}: {closest['closest_to_end']}")
        print()
    
    # Example of finding vertices with specific properties
    print("=== Vertices with Special Properties ===")
    
    # Find vertices that are close to at least one start point (distance <= 5)
    def close_to_start(vertex_idx, distances):
        return any(dist_tuple[0] <= 5 for dist_tuple in distances)
    
    close_vertices = find_vertices_with_specific_properties(distance_matrix, random_pairs, close_to_start)
    print(f"Vertices close to at least one start point (distance <= 5): {len(close_vertices)} vertices")
    print(f"First 10: {close_vertices[:10]}")
    
    return distance_matrix, random_pairs, stats

if __name__ == "__main__":
    distance_matrix, random_pairs, stats = main_analysis()
