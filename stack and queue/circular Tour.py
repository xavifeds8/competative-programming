petrol = [4, 7, 10, 4]
distance =[6, 6, 3, 5]
surplus = 0
deficit = 0
start = 0
for i in range(len(petrol)):
    surplus += petrol[i] - distance[i]
    if surplus <0:
        deficit += surplus
        surplus = 0 
        start = i+1
if surplus + deficit >= 0:
    print("we gotta start from" , start)
else:
    print("we cannot reach")
