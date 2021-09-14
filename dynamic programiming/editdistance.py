string1 = "intention"
string2 = "execution"

def editdist(string1 , string2 , i , j):
    if i==len(string1):
        return len(string2)-j
    if j==len(string2):
        return len(string1)-i
    if string1[i] == string2[j]:
        return editdist(string1 , string2 , i+1 , j+1)
    else: 
        insert = editdist(string1 , string2 ,i ,j+1)
        delete = editdist(string1 , string2 , i+1 , j)
        replace = editdist(string1 , string2 , i+1 , j+1)
        return 1+min(insert , delete , replace)
print(editdist(string1 , string2 , 0 ,0))