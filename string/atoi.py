string = "1234"
flag = 1
def (n):
    if n.isdigit():
        return ord(n) - 48
    else:
        return -1
res = 0
for i in string:
    if i == "-":
        flag = -1
        continue

    val = atoi(i)
    if val == -1:
        return -1
    res = res*10+val
print(res*flag)
