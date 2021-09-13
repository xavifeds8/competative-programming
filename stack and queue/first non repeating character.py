"""Given an input stream of A of n characters
consisting only of lower case alphabets
. The task is to find the first non repeating character,
each time a character is inserted to the stream.
If there is no such character then append '#' to the answer."""
A = "hrqcvsvszpsjammdrw"
d = {}
queue =[]
res = ""
for i in A:
    d[i] = d.get(i , 0)+1
    queue.append(i)
    if len(queue)==0 and d[queue[0]] == 1:
        res+=queue[0]
    else:
        while len(queue) and d[queue[0]] !=1:
            queue.pop(0)
        if len(queue):
            res+=queue[0]
        else:
            res+="#"
print(res)
