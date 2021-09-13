string = ["geeksforgeeks", "geeks", "geek" ,"geezer"]
def common(s1 , s2):
    for i in range(min(len(s1) , len(s2))):
        if s1[i] != s2[i]:
            return s1[:i]
    return s1
prefix = string[0]
for i in string:
    prefix = common(prefix , i)
print(prefix)
