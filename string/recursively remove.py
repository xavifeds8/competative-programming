"""
Given a string s, remove all its adjacent 
duplicate characters recursively """

#using stack 
def removeDuplicates(self, s: str) -> str:
    stack = []
    for i in s:
        if len(stack)==0 or stack[-1]!=i:
            stack.append(i)
        else:
            stack.pop(-1)
    return "".join(stack)
