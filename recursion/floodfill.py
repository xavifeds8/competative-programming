def disp(matrix):
    for i in matrix:
        print(i)
    print("----------")

image =[[1 , 1, 0] , [0 , 1, 0] , [1 , 1 , 1]]
disp(image)


def floodfill(grid , r , c , newCol , oldCol):
    if r>=len(grid) or r<0 or c>=len(grid[0]) or c<0:
        return 
    if grid[r][c] in [0 , newCol]:
        return 
    if grid[r][c] == oldCol:
        grid[r][c] = newCol
    x_path = [1 , -1 , 0 , 0]
    y_path = [0 , 0 , 1 , -1]
    for i in range(len(x_path)):
        floodfill(grid , r+x_path[i] , c+y_path[i] , newCol , oldCol)
floodfill(image , 0 , 0 , 2 , 1)
disp(image)