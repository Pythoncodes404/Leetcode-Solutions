class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here

        rows, cols = len(rooms), len(rooms[0])
        q = collections.deque()


        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    q.append((i,j))


        while q:

            length = len(q)

            for i in range(length):

                r,c = q.popleft()
                new_dist = rooms[r][c] + 1

                if r+1 < rows and rooms[r+1][c] == 2147483647:
                    rooms[r+1][c] = new_dist
                    q.append((r+1,c))
                
                if r-1 >=0 and rooms[r-1][c] == 2147483647:
                    rooms[r-1][c] = new_dist
                    q.append((r-1,c))
                
                if c+1 < cols and rooms[r][c+1] == 2147483647:
                    rooms[r][c+1] = new_dist
                    q.append((r,c+1))

                if c-1 >= 0 and rooms[r][c-1] == 2147483647:
                    rooms[r][c-1] = new_dist
                    q.append((r,c-1))                   

        return rooms