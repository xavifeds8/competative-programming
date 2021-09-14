valuelst = [60, 100 , 120]
weightlst = [10, 30 , 30]
W = 50

def knapsack(i , weight , W , value):
    if weight >= W:
        return 0
    if i == len(valuelst):
        return value
    return max(knapsack(i+1 , weight + weightlst[i] , W , value + valuelst[i]) , knapsack(i+1 , weight , W , value))
print(knapsack(0 , 0 , W , 0))