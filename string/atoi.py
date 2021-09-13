string = "1234"
def (n):
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
print(res)
