"""
Given a string s, remove all its adjacent 
duplicate characters recursively """

string = "acaaaaaaaaaaaabbbacdddd"
def recurse(string , i , last_removed):
    start = i
    end = i
    while string[i] == string[i+1]:
        i += 1
        end = i