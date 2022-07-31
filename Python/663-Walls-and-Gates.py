from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here

        rows, cols = len(rooms), len(rooms[0])
        neigh = [[1,0],[0,1],[-1,0],[0,-1]]
        q = collections.deque()


        def valid(r,c, prevR, prevC):
            if r in range(rows) and c in range(cols) and rooms[r][c] == 2147483647:
                        rooms[r][c] = rooms[prevR][prevC] + 1
                        q.append((r,c))


        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    q.append((i,j))

        
        while q:

            length = len(q)

            for i in range(length):

                r,c = q.popleft()
                valid(r+1,c,r, c)
                valid(r-1,c, r, c)
                valid(r,c+1, r, c)
                valid(r,c-1, r, c)                    

        return rooms