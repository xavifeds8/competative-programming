curr , prev , prev2 = 0 , 1 , 0
n = 5
for i in range(2 , n+2):
    curr = prev+prev2
    prev2 , prev = prev , curr
print(curr)

