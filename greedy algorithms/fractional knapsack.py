"""
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item. 
"""
W = 50
values = [60,100,120]
weight = [10,20,30]
items = sorted([[values[i]/weight[i] , weight[i]] for i in range(len(values))] , reverse= True)
print(items)
i = 0 
count = 0 
while W>=0:
    if items[i][1] < (W/items[i][0]):
        count += items[i][1]*items[i][0]
        W -= items[i][]
    else:
