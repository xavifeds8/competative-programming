def atoi(string):
    # Code here
    def atoi(n):
        if n.isdigit():
            return ord(n) - 48
        else:
            return -1
    res = 0
    for i in string:
        if i == "-":
            continue
            
        val = atoi(i)
        if val == -1:
            return -1
        res = res*10+val
    return res
print(atoi("12345asdfi"))