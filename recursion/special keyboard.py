"""
Imagine you have a special keyboard with the following keys: 

Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it 
after what has already been printed.

Find maximum numbers of A's that can be produced 
by pressing keys on the special keyboard N times. """


"""
we know that from 
1-> 6 we have to use A to maximize
AAAXCV --> 6
AAAAAA --> 6
7 --> AAAAAAA(7) < AAAXCVV(9)
8 --> AAAXCVVV (9)

"""
n = 10
dp = [i if i<=6 else 0 for i in range(n+1)]
for i in range(7 , n+1):
    for j in range(i-3 , 0 , -1):
        dp[i] = max(dp[i] , dp[j]*(i-j-1))
print(dp)
