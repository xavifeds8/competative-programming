from collections import Counter
s = "vieabievceiseivxxx"
pat = "vie"
c = Counter(pat)
k = len(pat)
cnt = 0 
for i in range(len(s)):
    if i<k:
        if s[i] in c:
            c[s[i]] -=1
    else:
        if s[i] in c:
            c[s[i]] -=1
        if s[i-k] in c:
            c[s[i-k]] +=1
    if sum(c.values())==0:
        cnt+=1
        print(s[i-k+1:i+1])
print(cnt)
    

    
