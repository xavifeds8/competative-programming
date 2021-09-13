string = "}"
stack = []
for i in string:
    if i in ["(","[","{"]:
        stack.append(i)
    else:
        if len(stack)==0 or stack.pop(-1)+i not in ["()","{}","[]"]:
            print("invalid parenthesis")
if len(stack):
    print("invalid parenthesis")
else:
    print("valid")
