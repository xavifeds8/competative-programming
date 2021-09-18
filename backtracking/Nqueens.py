n = 4
board = [[0 for _ in range(n)] for _ in range(n)]

def disphelper(matrix):
    for row in range(len(matrix)):
        print(row)
    print("--------------")


def Nqueens(board , n):
