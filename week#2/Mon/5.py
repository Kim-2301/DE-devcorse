def solution(x):
    if x == 0 or x==1:
        return x
    else :
        return solution(x-1)+solution(x-2)

def solution(x):
    ans=[0,1]
    if x == 0:
        return 0
    elif x == 1:
        return 1
    
    for i in range(2,x+1):
        ans.append(ans[i-1]+ans[i-2])
        
    return ans[-1]
