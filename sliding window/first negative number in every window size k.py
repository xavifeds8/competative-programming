lst = [12 , -1 , -7 , 8 , -15 ,1 ,3, 4 , -30 , 16 , 28 ,1 ]
k = 3
neglst = []
for i in range(k):
    if lst[i] <0:
        neglst.append(lst[i])
for i in range(k , len(lst)):
    if len(neglst)==0: 
        print(0)
    if lst[i] < 0: neglst.append(lst[i])
    if lst[i-k] != neglst[0]:
        print(neglst[0])
    else:
        print(neglst.pop(0))
    
