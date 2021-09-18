""""
You are given a string s of lower case english alphabets.
You can choose any two characters in the string and 
replace all the occurences of the first character with
the second character and replace all the occurences of
the second character with the first character. 
Your aim is to find the lexicographically smallest 
string that can be obtained by doing this operation 
at most once."""

string = "abba"
temp = sorted(set(string))
d = {}
for i in temp:
    d[i]  = i
for j in string:
    if d[j]