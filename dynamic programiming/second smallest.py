arr = [5  , 5 , 4 ,3 ,2,1,1]
sec_min = 10**9
first_min = 10**9
for i in range(len(arr)):
    if arr[i] in [sec_min , first_min]:
        continue
    if arr[i] < sec_min:
        sec_min = arr[i]
    if sec_min < first_min:
        sec_min , first_min = first_min , sec_min
print(sec_min)