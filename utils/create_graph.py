def create_graph(width=20,height=10,horizontal_weight=2,vertical_weight=1):

    # Parameters
    WIDTH = width  # horizontal streets
    HEIGHT = height  # vertical streets
    HORIZONTAL_WEIGHT = horizontal_weight
    VERTICAL_WEIGHT = vertical_weight

    # Create list of vertices (intersection points)
    vertices = []
    for row in range(HEIGHT):
        for col in range(WIDTH):
            vertex_index = row * WIDTH + col
            vertices.append((vertex_index, row, col))

    print(f"Total vertices: {len(vertices)}")
    print(f"First 10 vertices: {vertices[:10]}")

    # Create list of weighted edges
    edges = []

    # Add horizontal edges (connecting adjacent columns in same row)
    for row in range(HEIGHT):
        for col in range(WIDTH - 1):
            start_vertex = row * WIDTH + col
            end_vertex = row * WIDTH + (col + 1)
            edges.append((start_vertex, end_vertex, HORIZONTAL_WEIGHT))

    # Add vertical edges (connecting adjacent rows in same column)
    for row in range(HEIGHT - 1):
        for col in range(WIDTH):
            start_vertex = row * WIDTH + col
            end_vertex = (row + 1) * WIDTH + col
            edges.append((start_vertex, end_vertex, VERTICAL_WEIGHT))

    print(f"Total edges: {len(edges)}")
    print(f"Horizontal edges: {(HEIGHT) * (WIDTH - 1)}")
    print(f"Vertical edges: {(HEIGHT - 1) * WIDTH}")
    print(f"\nFirst 10 edges: {edges[:10]}")
    print(f"Last 10 edges: {edges[-10:]}")

    return edges, vertices