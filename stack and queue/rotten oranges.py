"""
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges
"""

grid = [[0,1,2],[0,1,2],[0,1,1]]
def disp(matrix):
    for i in matrix:
        print(i)
    print()
disp(grid)

queue = []

def bfs(grid):
    x_dir = [1 , -1 , 0 , 0]
    y_dir = [0 , 0 , -1 , 1]
    cnt = 0
    rottencnt = 0 
    while len(queue):
        l = len(queue)
        for i in range(l):
            rottencnt +=1
            p = queue.pop(0)
            x , y = p[0] , p[1]
            for i in range(len(x_dir)):
                r = x + x_dir[i] 
                c = y + y_dir[i]
                if r >= 0 and c>=0 and r<len(grid) and c<len(grid[0]):
                    if grid[r][c] == 1:
                        queue.append([r , c])
                        grid[r][c] = 2
        if len(queue):cnt+=1
    return [cnt , rottencnt]




def bfshelper(grid):
    totalOranges = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2 or grid[i][j] == 1:
                totalOranges +=1
                if grid[i][j] == 2:
                    queue.append([i , j])
                
    days , rotcnt =bfs(grid)
    if rotcnt != totalOranges:
        print(-1)
    else:
        print("the number of days were" , days)
bfshelper(grid)