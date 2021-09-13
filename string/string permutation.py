string = "ABC"
def per(string , i):
    if i == len(string)-1:
        print("".join(string))
        return 
    for j in range(i , len(string)):
        string[i] , string[j] = string[j] , string[i]
        per(string , i+1)
        string[i] , string[j] = string[j] , string[i]
per(list(string) , 0)
    