def isCyclicUtil(node, visited, parent, edges):
     
        # Mark the current node as visited
        visited[node] = True
 
        # Recur for all the vertices
        # adjacent to this vertex
        for i in edges:
 
            # If the node is not
            # visited then recurse on it
            if visited[i] == False:
                if(isCyclicUtil(i, visited, node, edges)):
                    return True
            # If an adjacent vertex is
            # visited and not parent
            # of current vertex,
            # then there is a cycle
            elif parent != i:
                return True
 
        return False
 
    # Returns true if the graph
    # contains a cycle, else false.
 
def isCyclic(edges, nodes):

    # Mark all the vertices
    # as not visited
    visited = [False] * (nodes)

    # Call the recursive helper
    # function to detect cycle in different
    # DFS trees
    for i in range(nodes):
        # Don't recur for u if it
        # is already visited
        if visited[i] == False:
            if(isCyclicUtil(i, visited, -1, edges)) == True:
                return True

    return False