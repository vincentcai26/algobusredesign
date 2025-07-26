from utils.create_graph import create_graph
from route_plotting import plot_routes_on_graph, plot_single_route

# Create the graph
edges, vertices = create_graph()

# Example routes (lists of vertex indices in order)
example_routes = [
    [0, 1, 2, 22, 42, 62],  # Route 1: horizontal then vertical
    [199, 179, 159, 158, 157, 137, 117],  # Route 2: from bottom-right
    [10, 30, 50, 51, 52, 53]  # Route 3: mixed path
]

# Plot multiple routes
plot_routes_on_graph(vertices, edges, example_routes)

# Plot a single route
single_route = [0, 1, 2, 3, 4, 24, 44, 64, 84]
plot_single_route(vertices, edges, single_route, "L-Shaped Route Example")