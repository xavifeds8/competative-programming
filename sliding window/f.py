from collections import Counter
import collections


s = "aabdbddbaadadddaaaaaaaaaaaaaaaaaaa"
se = set(s)
max_val , x = -1 , ""
for i in se:
    if s.count(i)>max_val:
        max_val , x = s.count(i) , i
print(max_val , x)