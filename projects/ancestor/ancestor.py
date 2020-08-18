from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    # Target first and second value within ancestors list
    # Add each value as a vertex on our Graph
    for (v1, v2) in ancestors:
        g.add_vertex(v1)
        g.add_vertex(v2)

    # Create edges for each set of values
    for (v1, v2) in ancestors:
        g.add_edge(v1, v2)

    # Keep track of node's greatest ancestor
    depth = 1
    target_ancestor = None

    for val in g.vertices:
        # Build path from val to starting_node
        # by utilizing dfs
        path = g.dfs(val, starting_node)

        # If path length greater than current depth
        # reassign depth value to new path length
        if path:
            if len(path) > depth:
                depth = len(path)
                target_ancestor = val

        # If no path to starting_node
        elif not path and depth == 1:
            target_ancestor = -1

    return target_ancestor
