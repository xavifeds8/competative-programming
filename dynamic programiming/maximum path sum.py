matrix = [[ 10, 10, 2, 0, 20, 4 ],
        [ 1, 0, 0, 30, 2, 5 ],
        [ 0, 10, 4, 0, 2, 0 ],
        [ 1, 0, 2, 20, 0, 4 ]]

def maxPathSum(i , j , string):
    if i>len(matrix)-1 or j>len(matrix[0])-1:
        return -10**9
    if i==len(matrix)-1 and j==len(matrix[0])-1:
        print(string)
        return matrix[-1][-1]
    return matrix[i][j] + max(maxPathSum(i+1 , j , string+"D") , maxPathSum(i , j+1 , string+"R"))
print(maxPathSum(0 , 0 , ""))