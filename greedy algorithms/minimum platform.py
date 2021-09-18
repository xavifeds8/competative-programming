arr = [900 , 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
arr.sort()
dep.sort()
arrptr = 1
depptr = 0
count = 1 
max_count = 1
while arrptr<len(arr):
    if dep[depptr] >= arr[arrptr]:
        print(count)
        count +=1 
    else:
        depptr +=1
    max_count = max(max_count , count)
    arrptr+=1
print(count)