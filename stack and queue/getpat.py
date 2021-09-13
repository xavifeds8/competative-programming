matrix = [["o" , "b" ,"b"] , ["b" , "o" , "b"] , ["b" , "b" , "o"]]
# x.append(list(input().split()))
def disp(matrix):
    for i in matrix:
        print(i)
    print("--------")
def check(x,y):
    x_dir = [1 , 1, 1, 0 , 0 , -1 , -1 , -1 ]
    y_dir = [-1, 0 ,1 ,-1 ,1 , -1 , 0 ,  1]
    res = 0
    for i in range(len(x_dir)):
        if x+x_dir[i] >= 0 and x+x_dir[i] <len(matrix)  and y+y_dir[i] >= 0 and y+y_dir[i] <len(matrix):
            if matrix[x+x_dir[i]][y+y_dir[i]] == "b":
                res+=1
    return res
        

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == "o":
            matrix[i][j] = check(i , j)
disp(matrix)

    