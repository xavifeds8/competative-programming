"""
Given two numbers 'N' and 'S' ,
find the largest number that can be formed with 'N' 
digits and whose sum of digits should be equals to 'S'."""

N = 3
S = 28
sum_ = 0 
res = ""
while N >0:
    if sum_ == S:
        while N > 0:
            res+="0"
            N-=1
        print(res)
        break
    elif sum_ < S:
        if sum_ + 9 > S:
            res+= str(S - sum_)
            N-=1
            while N > 0:
                res+="0"
                N-=1
            print(res)
            break
        res += "9"
        sum_ += 9 
        N-=1
if sum_ != S:
    print(-1)

        

