"""
Given an input string and a dictionary of words, 
find out if the input string can be segmented into a 
space-separated sequence of dictionary words.
See following examples for more details. 
"""

"""
if word[:i] is in the dictionary 
return true if word[i:] is in the dictionary as well
"""

string = "icecreammobile"
s = {"mobile","samsung","sam","sung",
    "man","mango","icecream","and",
        "go","i","like","ice","cream"}

def wordBreak(string):
    if len(string) == 0: return True

    else:

        return any([(string[:i] in s) and wordBreak(string[i:]) for i in range(1 , len(string)+1)])
print(wordBreak(string))
def disp(matrix):
    for i in matrix:
        print(i)
    print("------------")  
def dynamic(string):
    dp = [0 for i in range(len(string)+1)]
    for i in range(1 , len(dp)):
        if dp[i-1] == 1 and string
