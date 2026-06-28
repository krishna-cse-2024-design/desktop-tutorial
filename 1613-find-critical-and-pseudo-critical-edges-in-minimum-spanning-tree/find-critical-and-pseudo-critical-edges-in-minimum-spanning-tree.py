class UnionFind:
    # Constructor to initialize the Union-Find structure with n elements.
    def __init__(self, n):
        # Each element is its own parent initially.
        self.parent = list(range(n))
    
    # Find function with path compression optimization.
    # This function returns the root parent of the element p.
    def find_parent(self, p):
        # If the element is its own parent, return it.
        if self.parent[p] == p:
            return p
        # Otherwise, recursively find the root parent and compress the path.
        self.parent[p] = self.find_parent(self.parent[p])
        return self.parent[p]
    
    # Union function to merge two sets (u and v).
    def union(self, u, v):
        # Find the root parents of u and v.
        pu, pv = self.find_parent(u), self.find_parent(v)
        # Make the root of u point to the root of v (merge them).
        self.parent[pu] = pv

class Solution:
    # Main function to find critical and pseudo-critical edges in a graph.
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Helper function to compare edges based on weight.
        def cmp(a, b):
            return a[2] < b[2]  # Compare the third element (weight) of each edge.
        
        critical, pseudo_critical = [], []  # To store critical and pseudo-critical edges.
        
        # Append index of each edge to keep track of their original position.
        for i in range(len(edges)):
            edges[i].append(i)
        
        # Sort edges by weight.
        edges.sort(key=lambda x: x[2])
        
        # Find the weight of the minimum spanning tree (MST) without blocking any edge.
        mst_wt = self.find_mst(n, edges, -1, -1)
        
        # Iterate through each edge to determine if it's critical or pseudo-critical.
        for i in range(len(edges)):
            # If excluding this edge results in a higher MST weight, it's critical.
            if mst_wt < self.find_mst(n, edges, i, -1):
                critical.append(edges[i][3])  # Append the original index of the edge.
            # If including this edge results in the same MST weight, it's pseudo-critical.
            elif mst_wt == self.find_mst(n, edges, -1, i):
                pseudo_critical.append(edges[i][3])  # Append the original index of the edge.
        
        # Return the list of critical and pseudo-critical edges.
        return [critical, pseudo_critical]
    
    # Function to find the weight of the MST, optionally blocking or forcing an edge.
    def find_mst(self, n, edges, block, e):
        # Initialize the Union-Find structure for n nodes.
        uf = UnionFind(n)
        weight = 0  # Track the total weight of the MST.
        
        # If edge 'e' is forced, add it to the MST.
        if e != -1:
            weight += edges[e][2]  # Add the weight of the forced edge.
            uf.union(edges[e][0], edges[e][1])  # Union the vertices of the forced edge.
        
        # Iterate through all edges to construct the MST.
        for i in range(len(edges)):
            # Skip the edge if it's blocked.
            if i == block:
                continue
            # Skip the edge if it forms a cycle.
            if uf.find_parent(edges[i][0]) == uf.find_parent(edges[i][1]):
                continue
            # Union the vertices and add the edge's weight to the MST.
            uf.union(edges[i][0], edges[i][1])
            weight += edges[i][2]
        
        # Check if all vertices are connected (i.e., a valid MST).
        for i in range(n):
            if uf.find_parent(i) != uf.find_parent(0):
                return float('inf')  # Return infinity if the graph is not connected.
        
        # Return the total weight of the MST.
        return weight