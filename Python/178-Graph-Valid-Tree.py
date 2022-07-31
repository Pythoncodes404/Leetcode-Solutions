from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here

        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges) + 1)

        def find(n):

            p = parent[n]

            while p!= parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        def union(n1, n2):

            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]

            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return 1

        res = n - 1
        for n1, n2 in edges:
            if not union(n1,n2):
                return False
            else:
                res -= 1

        return True if not res else False