def disp(matrix):
    for i in matrix:
        print(i)
    print("--------")
m = 3
n = 3
paths = [[0 for i in range(n)] for j in range(m)]

def numberOfPaths(m , n , r , c):
    if r == m-1 and c == n-1:
        print("reached")
        paths[-1][-1] = 1
        disp(paths)
        return 
    if r>=m or r<0 or c>=n or c<0:
        return
    paths[r][c] = 1
    numberOfPaths(m, n , r+1 , c)
    numberOfPaths(m , n , r , c+1)
    paths[r][c] = 0
# numberOfPaths(m , n , 0 , 0)


def numberOfpathsdp()


