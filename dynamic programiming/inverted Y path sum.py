"""
find max path from row = 0 , to row = n-1
can move down , diagonal left or right"""
matrix = [[ 10, 10, 2, 0, 20, 4 ],
        [ 1, 0, 0, 30, 2, 5 ],
        [ 0, 10, 4, 0, 2, 0 ],
        [ 1, 0, 2, 20, 0, 4 ]]
def sumYpath(i , j):
    if i >= len(matrix) or j>= len(matrix[0]) or i <0 or j<0:
        return -10**9
    if i==len(matrix)-1:
        return matrix[i][j]
    a = sumYpath(i+1 , j)
    b = sumYpath(i+1 , j-1)
    c = sumYpath(i+1 , j+1)
    return matrix[i][j] + max(a , b , c)
val = -1
for x in range(len(matrix[0])):
    val = max(val , sumYpath(0 , x))
print(val)
