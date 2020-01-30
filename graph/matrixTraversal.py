'''
We are given a matrix that contains different values in its each cell. Our aim is to find the minimal set of positions 
in the matrix such that entire matrix can be traversed starting from the positions in the set. We can traverse 
the matrix under below conditions:
We can move only to those neighbors that contain value less than or to equal to the current cell’s value. 
A neighbor of cell is defined as the cell that shares a side with the given cell.

Examples:

Input : 1 2 3
        2 3 1
        1 1 1
Output : 1 1
         0 2

If we start from 1, 1 we can cover 6 
vertices in the order (1, 1) -> (1, 0) -> (2, 0) 
-> (2, 1) -> (2, 2) -> (1, 2). We cannot cover
the entire matrix with this vertex. Remaining 
vertices can be covered (0, 2) -> (0, 1) -> (0, 0).
'''
def dfs(matrix, i, j, visited):
    visited[i][j] = 1
    if i - 1 > 0 and not visited[i-1][j] and matrix[i-1][j] <= matrix[i][j]:
        dfs(matrix, i - 1, j, visited)
    if i + 1 < len(matrix) and not visited[i+1][j] and matrix[i+1][j] <= matrix[i][j]:
        dfs(matrix, i + 1, j, visited)
    if j - 1 > 0 and not visited[i][j-1] and matrix[i][j - 1] <= matrix[i][j]:
        dfs(matrix, i, j - 1, visited)
    if j + 1 < len(matrix[0]) and not visited[i][j+1] and matrix[i][j+1] <= matrix[i][j]:
        dfs(matrix, i, j + 1, visited)        

def minVertices(matrix):
    max_val = -1
    for row in matrix:
        for i in row:
            if i > max_val:
                max_val = i
    visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == max_val and not visited[i][j]:
                print(i, j)
                dfs(matrix, i, j, visited)

matrix = [[1, 2, 3],  [2, 3, 1], [1, 1, 1]]
minVertices(matrix)