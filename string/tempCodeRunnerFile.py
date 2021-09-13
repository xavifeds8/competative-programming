ge(len(S)):
    if S[j] in d:
        i = d[S[j]] + 1
    d[S[j]] = j
print(j-i+1 , S